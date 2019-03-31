import itertools
import time

start_time = time.time()
iter_bestvalue = []
num_cities = 50
num_stops = 6
exact_minimum = 10000
mini_route = []
exhasted_salesman = traveling_salesman(num_cities)

cities = np.arange(num_cities)
all_combinations = itertools.combinations(cities, num_stops)
combinations_array = np.array(list(all_combinations))

for i in range(combinations_array.shape[0]):
    all_routes = itertools.permutations(combinations_array[i], num_stops)
    routes_array = np.array(list(all_routes))

    for j in range(routes_array.shape[0]):
        salesman.new_tour(tour=routes_array[j])
        length = salesman.tour_length()

        if length < exact_minimum:
            exact_minimum = length
            mini_route = list(routes_array[j])
            iter_bestvalue.append(exact_minimum)

print("--- %s seconds ---" % (time.time() - start_time))
print("Exhausted algorithm exact minimum route: ", mini_route)
print("Exhausted algorithm minumum distance = %f" % (exact_minimum))

salesman.new_tour(tour=mini_route)
salesman.plot()

plt.plot(iter_bestvalue, color='b')
plt.title('Exhausted Search')
plt.xlabel('Updated times')
plt.ylabel('Optimized value')
plt.grid(linewidth="0.2")