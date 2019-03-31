def RandomSearch(problem, x, y, x_best, y_best):
    random_num = 1000

    x_prime = np.random.choice(x, size=random_num, replace=True, p=None)
    y_prime = np.random.choice(x, size=random_num, replace=True, p=None)

    for i in range(random_num):
        if problem == 0:
            z_best = toy_problem_0(x_best, y_best)
            z_prime = toy_problem_0(x_prime[i], y_prime[i])
            z_value[0][i] = z_best
        elif problem == 1:
            z_best = toy_problem_1(x_best, y_best)
            z_prime = toy_problem_1(x_prime[i], y_prime[i])
            z_value[1][i] = z_best
        elif problem == 2:
            z_best = toy_problem_2(x_best, y_best)
            z_prime = toy_problem_2(x_prime[i], y_prime[i])
            z_value[2][i] = z_best
        else:
            z_best = toy_problem_3(x_best, y_best)
            z_prime = toy_problem_3(x_prime[i], y_prime[i])
            z_value[3][i] = z_best

        if z_prime < z_best:
            x_best = x_prime[i]
            y_best = y_prime[i]
            z_best = z_prime

    return (x_best, y_best, z_best)


x_best = 15
y_best = 15
random_num = 1000
z_value = np.zeros((4, random_num))

x0_opt, y0_opt, z0_opt = RandomSearch(0, x, y, x_best, y_best)
x1_opt, y1_opt, z1_opt = RandomSearch(1, x, y, x_best, y_best)
x2_opt, y2_opt, z2_opt = RandomSearch(2, x, y, x_best, y_best)
x3_opt, y3_opt, z3_opt = RandomSearch(3, x, y, x_best, y_best)

print("Problem 0: Optimized result = %f, x = %10.1f, y = %10.1f" % (z0_opt, x0_opt, y0_opt))
print("Problem 1: Optimized result = %f, x = %10.1f, y = %10.1f" % (z1_opt, x1_opt, y1_opt))
print("Problem 2: Optimized result = %f, x = %10.1f, y = %10.1f" % (z2_opt, x2_opt, y2_opt))
print("Problem 3: Optimized result = %f, x = %10.1f, y = %10.1f" % (z3_opt, x3_opt, y3_opt))

# T1_Q3_BONUS
plt.figure(1)
plt.plot(z_value[0], color = 'b')
plt.title('Toy problem 0')
plt.xlabel('ramdom num')
plt.ylabel('optimized result')
y_ticks = np.arange(0, 450, 50)
plt.yticks(y_ticks)
plt.grid(linewidth = "0.3")

plt.figure(2)
plt.plot(z_value[1], color = 'g')
plt.title('Toy problem 1')
plt.xlabel('ramdom num')
plt.ylabel('optimized result')
plt.grid(linewidth = "0.3")

plt.figure(3)
plt.plot(z_value[2], color = 'r')
plt.title('Toy problem 2')
plt.xlabel('ramdom num')
plt.ylabel('optimized result')
y_ticks = np.arange(-15, 10, 2)
plt.yticks(y_ticks)
plt.grid(linewidth = "0.3")

plt.figure(4)
plt.plot(z_value[3], color = 'c')
plt.title('Toy problem 3')
plt.xlabel('ramdom num')
plt.ylabel('optimized result')
y_ticks = np.arange(-5, 20, 2)
plt.yticks(y_ticks)
plt.grid(linewidth = "0.3")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)