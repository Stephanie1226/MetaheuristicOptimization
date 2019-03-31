# Code for T2Q2
import time


class genetic_algorithm():
    def __init__(self, mating_pool, population_size, stops):
        self.mating_pool = mating_pool
        self.stops = stops
        self.population_size = population_size
        self.fitness = np.zeros(len(mating_pool))
        self.probability = np.zeros(len(mating_pool))
        self.pc = 0.0  # Probability of performing crossover, pc = 0.6~1.0
        self.pm = 0.05  # pm = 0.005~0.05

    # This "random_pick func" is for random selection according to different probability using after calculate fitness funtion
    def random_pick(self, some_list, probabilities):
        random.seed(time.time())
        x = random.uniform(0, 1)
        cumulative_probability = 0.0
        for item, item_probability in zip(some_list, probabilities):
            cumulative_probability += item_probability
            if x < cumulative_probability: break
        return (item)

    def parent_choose(self, distance):
        self.distance = distance
        pro_denominator = 0
        counter = 0
        new_pop_list = []
        select_population = np.zeros((1, self.stops))
        pop_index = list(range(0, self.population_size))

        # Fitness function
        for i in range(self.population_size):
            self.fitness[i] = 1 / self.distance[i]
            pro_denominator = pro_denominator + self.fitness[i]

        self.pc = round(random.uniform(0.6, 1.0),
                        1)  # Randomly pick a num for "probability of performing crossover", pc = 0.6~1.0

        for j in range(
                self.population_size):  # Probability is the reciprocal of fitness function divided by the sum of fitness function
            self.probability[j] = self.fitness[j] / pro_denominator

        while (
                counter < self.pc * self.population_size):  # "self.pc*self.population_size" is the amount of chosen parents(population)
            # Random pick a route(depends on different probability)
            index = self.random_pick(pop_index, self.probability)
            if (index not in new_pop_list):  # Add the chosen route to the cosen population
                new_pop_list.append(index)
                select_pop = self.mating_pool[index]
                select_population = np.row_stack((select_population, select_pop[None, :]))
                counter += 1
        select_population = np.delete(select_population, 0, axis=0)
        return (select_population)

    # Produce offspring through chosen parents
    def crossover(self, select_p):
        new_mating_pool = np.zeros((1, self.stops))
        count = 0
        while (count < select_p.shape[0]):  # For each pair in chosen parents, do crossover to produce 2 offsprings
            random.seed(time.time())
            choose = random.randint(0, self.stops)
            parent_A = select_p[count]
            parent_B = select_p[count + 1]

            # For each parents, this is the first offspring
            gene_a1 = parent_A[: choose]
            gene_a2 = [x for x in parent_B if x not in gene_a1]
            childA = np.concatenate((gene_a1, gene_a2), axis=0)
            new_mating_pool = np.row_stack((new_mating_pool, childA[None, :]))

            # For each parents, this is the second offspring
            gene_b1 = parent_B[: choose]
            gene_b2 = [x for x in parent_A if x not in gene_b1]
            childB = np.concatenate((gene_b1, gene_b2), axis=0)
            new_mating_pool = np.row_stack((new_mating_pool, childB[None, :]))

            count += 2  # Next pair of parents
        new_mating_pool = np.delete(new_mating_pool, 0, axis=0)
        return (new_mating_pool)

    def mutation(self, pool):
        for i in range(pool.shape[0]):
            random.seed(time.time())
            random_num = random.random()

            if (random_num < self.pm):
                mutate_1 = random.randint(0, self.stops - 1)
                while True:
                    mutate_2 = random.randint(0, self.stops - 1)
                    if mutate_1 != mutate_2:
                        break
                temp_gene = pool[i]
                temp1 = temp_gene[mutate_1]
                temp_gene[mutate_1] = temp_gene[mutate_2]
                temp_gene[mutate_2] = temp1
                pool[i] = temp_gene
        return (pool)

    def new_population(self, pre_pool):
        new_pool = pre_pool
        num = self.population_size - pre_pool.shape[0]
        for i in range(num):
            index = np.argmin(self.distance)
            new_pool = np.row_stack((new_pool, self.mating_pool[index]))
            np.delete(self.distance, index)
        return (new_pool)


# Main function (time start)
start_time = time.time()

num_cities = 50
pop_size = 20
num_stops = 50
iterations = 2000

# Initialize salesman problem
salesman = traveling_salesman(num_cities)  # initialize the TS's world with 50 cities
# Initialize population, distance
mating_pool = np.zeros((pop_size, num_stops))
distance = np.zeros(pop_size)

# Randomly generate a numbers of routes, calculate their distance
for i in range(pop_size):
    mating_pool[i] = salesman.random_tour(num_stops)
    distance[i] = salesman.tour_length()

for i in range(iterations):
    genetic_alg = genetic_algorithm(mating_pool, pop_size, num_stops)
    # Select parents
    selected_population = genetic_alg.parent_choose(distance)
    # Crossover
    mating_pool = genetic_alg.crossover(selected_population)
    # Mutation
    mating_pool = genetic_alg.mutation(mating_pool)

    if (mating_pool.shape[0] < pop_size):
        mating_pool = genetic_alg.new_population(mating_pool)

    for i in range(pop_size):
        salesman.new_tour(tour=mating_pool[i])
        distance[i] = salesman.tour_length()

# Find the minimized 50-city route in whole population
min_index = np.argmin(distance)
min_route_50 = mating_pool[min_index]
min_dis_6 = 1000

# Check every 6-city route in minimized 50-city route
for i in range(num_stops - 6):
    route_6 = min_route_50[i: i + 6]
    salesman.new_tour(tour=route_6)
    dis_6 = salesman.tour_length()

    if (dis_6 < min_dis_6):
        min_dis_6 = dis_6
        min_route_6 = min_route_50[i: i + 6]

print("--- %s seconds ---" % (time.time() - start_time))

salesman.new_tour(tour=min_route_6)
min_route_6 = list(map(int, min_route_6))
print("The best route of 6 cities: ", min_route_6)
print("The minimum distance of 6 cities: ", min_dis_6)
salesman.plot()