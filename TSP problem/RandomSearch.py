import time

start_time = time.time()
random_num = np.power(10, 7)
random_minumum = 10000
random_length = 0
random_bestvalue = []

salesman = traveling_salesman(num_cities=50)

for i in range(random_num):
    random_tour = salesman.random_tour(num_stops=6)
    random_length = salesman.tour_length()

    if (random_length < random_minumum):
        random_minumum = random_length
        random_min_tour = random_tour
        random_bestvalue.append(random_minumum)

print("--- %s seconds ---" % (time.time() - start_time))

print("Random algorithm minimum route: ", random_min_tour)
print("Random algorithm minumum distance = %f" % (random_minumum))
salesman.new_tour(tour=random_min_tour)
salesman.plot()

plt.plot(random_bestvalue, color='b')
plt.title('Random Search')
plt.xlabel('Updated times')
plt.ylabel('Optimized value')
my_x_ticks = np.arange(0, 19, 1)
plt.xticks(my_x_ticks)
plt.grid(linewidth="0.2")