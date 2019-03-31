step_task2_0 = []
step_task2_1 = []
step_task2_2 = []
step_task2_3 = []

def ObjectFunc(pro, step_s, x, y, gx, gy):
    if pro == 0:
        value = toy_problem_0((x - step_s * gx), (y - step_s * gy))
    elif pro == 1:
        value = toy_problem_1((x - step_s * gx), (y - step_s * gy))
    elif pro == 2:
        value = toy_problem_2((x - step_s * gx), (y - step_s * gy))
    else:
        value = toy_problem_3((x - step_s * gx), (y - step_s * gy))
    return value

def StepSearch(pro, x, y, g_x, g_y):
    stepsize = 0
    step_search = np.linspace(0, 1, 100)
    min_Objectfunc = ObjectFunc(pro, step_search[0], x, y, g_x, g_y)
    for i in range(len(step_search)):
        new_Objectfunc = ObjectFunc(pro, step_search[i], x, y, g_x, g_y)
        if (new_Objectfunc < min_Objectfunc):
            min_Objectfunc = new_Objectfunc
            stepsize = step_search[i]
    if pro == 0:
        step_task2_0.append(stepsize)
    elif pro == 1:
        step_task2_1.append(stepsize)
    elif pro == 2:
        step_task2_2.append(stepsize)
    else:
        step_task2_3.append(stepsize)
    return stepsize

def GradientDescent(problem, x, y):
    h = 0.1
    if problem == 0:
        gradient_x = (toy_problem_0(x + h, y) - toy_problem_0(x - h, y)) / (2 * h)
        gradient_y = (toy_problem_0(x, y + h) - toy_problem_0(x, y - h)) / (2 * h)
    elif problem == 1:
        gradient_x = (toy_problem_1(x + h, y) - toy_problem_1(x - h, y)) / (2 * h)
        gradient_y = (toy_problem_1(x, y + h) - toy_problem_1(x, y - h)) / (2 * h)
    elif problem == 2:
        gradient_x = (toy_problem_2(x + h, y) - toy_problem_2(x - h, y)) / (2 * h)
        gradient_y = (toy_problem_2(x, y + h) - toy_problem_2(x, y - h)) / (2 * h)
    else:
        gradient_x = (toy_problem_3(x + h, y) - toy_problem_3(x - h, y)) / (2 * h)
        gradient_y = (toy_problem_3(x, y + h) - toy_problem_3(x, y - h)) / (2 * h)

    step = StepSearch(problem, x, y, gradient_x, gradient_y)
    x = x - gradient_x * step
    y = y - gradient_y * step

    return (x, y)


def CalOptimizedValue(count, x, y):
    if count == 0:
        value = toy_problem_0(x, y)
    elif count == 1:
        value = toy_problem_1(x, y)
    elif count == 2:
        value = toy_problem_2(x, y)
    else:
        value = toy_problem_3(x, y)

    return value


# Main
toyproblem = 4
iterations = 50
tolerance = 1e-6
z_task2_0 = []
z_task2_1 = []
z_task2_2 = []
z_task2_3 = []

for count in range(toyproblem):
    x_best = 15
    y_best = 15
    itera = 0
    z_pre = 0
    z_best = CalOptimizedValue(count, x_best, y_best)
    if count == 0:
        z_task2_0.append(z_best)
    elif count == 1:
        z_task2_1.append(z_best)
    elif count == 2:
        z_task2_2.append(z_best)
    else:
        z_task2_3.append(z_best)

    while (itera < iterations) and (abs(z_best - z_pre) > tolerance):
        z_best = CalOptimizedValue(count, x_best, y_best)
        z_pre = z_best
        x_best, y_best = GradientDescent(count, x_best, y_best)

        z_best = CalOptimizedValue(count, x_best, y_best)
        if count == 0:
            z_task2_0.append(z_best)
        elif count == 1:
            z_task2_1.append(z_best)
        elif count == 2:
            z_task2_2.append(z_best)
        else:
            z_task2_3.append(z_best)

        itera += 1

    print("This is the toy problem %d" % (count))
    print("--> x = " + str(x_best))
    print("--> y = " + str(y_best))
    print("--> Optimized value = " + str(z_best))

    
#plot
plt.figure(1)
plt.plot(z_task2_0, color = 'b')
plt.title('toy problem 0')
plt.xlabel('Iterations')
plt.ylabel('optimized result')
plt.grid(linewidth = "0.3")

plt.figure(2)
plt.plot(z_task2_1, color = 'g')
plt.title('toy problem 1')
plt.xlabel('Iterations')
plt.ylabel('optimized result')
plt.grid(linewidth = "0.3")

plt.figure(3)
plt.plot(z_task2_2, color = 'r')
plt.title('toy problem 2')
plt.xlabel('Iterations')
plt.ylabel('optimized result')
plt.grid(linewidth = "0.3")

plt.figure(4)
plt.plot(z_task2_3, color = 'c')
plt.title('toy problem 3')
plt.xlabel('Iterations')
plt.ylabel('optimized result')
plt.grid(linewidth = "0.3")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)