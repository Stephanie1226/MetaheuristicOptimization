# Code for T3Q2
import time

class differential_algorithm():
    def __init__(self, p_pool, p_size, n_cities):
        self.pop_pool = p_pool
        self.pop_size = p_size
        self.cities_number = n_cities
        self.tour = None
        self.F = 0.5  # F is a real-valued factor in the range (0.0, 2]
        self.cr = 0.07  # CR is a real-valued crossover constant in the range [0.0,1.0]

    # mutation part
    def mutation(self, count):
        # Randomly choose three routes for differential claculation
        index_num = np.arange(0, self.pop_size, 1)
        choose = random.sample(list(index_num), 3)

        # Do the calculation: temp_new = x1 + F*(x2 - x3)
        temp_new = self.pop_pool[choose[0]] + self.F * (self.pop_pool[choose[1]] - self.pop_pool[choose[2]])
        temp_new = np.argsort(temp_new)
        return temp_new

    def crossover(self, number, temp):
        new = np.ones((1, self.cities_number)) * 100
        list_index = []

        # For each city in the one route
        for j in range(self.cities_number):
            rand_num = random.random()
            # Randomly select a number from [0, 1], if the rand number is smaller than "crossover probability",
            # take the value from "temp_new" in mutation part
            if (rand_num < self.cr):
                new[0][j] = temp[j]
            # Otherwise, take the value from previous route
            else:
                list_index.append(j)

        # To avoid repeated value in a route
        not_repeat = [x for x in self.pop_pool[number] if x not in new]
        for k in range(len(list_index)):
            new[0][list_index[k]] = not_repeat[k]

        return new


# Main function (time start)
start_time = time.time()

num_cities = 50
pop_size = 80  # population size
num_stops = 50
iterations = 10000

# Initialize salesman problem
salesman = traveling_salesman(num_cities)  # initialize the TS's world with 50 cities
# Initialize population and population distance
population_pool = np.zeros((pop_size, num_stops))
route_distance = np.zeros(pop_size)

# Randomly generate a numbers of routes, calculate their distance
for i in range(pop_size):
    population_pool[i] = salesman.random_tour(num_stops)
    route_distance[i] = salesman.tour_length()

for i in range(iterations):
    differential_alg = differential_algorithm(population_pool, pop_size, num_cities)

    # For every route in population pool, do mutation and crossover
    for k in range(pop_size):
        temp = differential_alg.mutation(k)
        new = differential_alg.crossover(k, temp)
        temp_new = new.flatten().tolist()

        salesman.new_tour(tour=temp_new)
        temp_dis = salesman.tour_length()

        # If the new one is better, replace the previous one with the new one. Otherwise, don't change it.
        if (temp_dis < route_distance[k]):
            population_pool[k] = new
            route_distance[k] = temp_dis

print("--- %s seconds ---" % (time.time() - start_time))

# Find the minimized 50-city route in whole population
min_route_index = np.argmin(route_distance)
DE_mintour_50 = population_pool[min_route_index]

# Check every 6-city route in minimized 50-city route
min_dedis_6 = 150
for i in range(num_stops - 6):
    DE_route_6 = DE_mintour_50[i: i + 6]
    salesman.new_tour(tour=DE_route_6)
    de_dis_6 = salesman.tour_length()

    if (de_dis_6 < min_dedis_6):
        min_dedis_6 = de_dis_6
        min_de_route_6 = DE_mintour_50[i: i + 6]

salesman.new_tour(tour=min_de_route_6)
de_min_route = list(map(int, min_de_route_6))
print("The best route of 6 cities: ", de_min_route)
print("The minimum distance of 6 cities: ", min_dedis_6)
salesman.plot()