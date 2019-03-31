# T3Q2
def ObjectFunc(pro, step_s, x, g_k, h_k):
    d = -1.0 * np.dot(h_k, g_k)
    x = x + step_s * d
    if pro == 0:
        value = toy_problem_0(x[0][0], x[1][0])
    elif pro == 1:
        value = toy_problem_1(x[0][0], x[1][0])
    elif pro == 2:
        value = toy_problem_2(x[0][0], x[1][0])
    else:
        value = toy_problem_3(x[0][0], x[1][0])
    return value

def StepSearch(pro, x, gk, hk):
    stepsize = 0
    step_search = np.linspace(0, 1, 100)
    min_Objectfunc = ObjectFunc(pro, step_search[0], x, gk, hk)
    for i in range(len(step_search)):
        new_Objectfunc = ObjectFunc(pro, step_search[i], x, gk, hk)
        if (new_Objectfunc < min_Objectfunc):
            min_Objectfunc = new_Objectfunc
            stepsize = step_search[i]
    return stepsize

def FirstGrad(pro, x0, x1):
    grad = np.zeros((2, 1))
    h = 0.1
    if pro == 0:
        gradient_x = (toy_problem_0(x0 + h, x1) - toy_problem_0(x0 - h, x1)) / (2 * h)
        gradient_y = (toy_problem_0(x0, x1 + h) - toy_problem_0(x0, x1 - h)) / (2 * h)
    elif pro == 1:
        gradient_x = (toy_problem_1(x0 + h, x1) - toy_problem_1(x0 - h, x1)) / (2 * h)
        gradient_y = (toy_problem_1(x0, x1 + h) - toy_problem_1(x0, x1 - h)) / (2 * h)
    elif pro == 2:
        gradient_x = (toy_problem_2(x0 + h, x1) - toy_problem_2(x0 - h, x1)) / (2 * h)
        gradient_y = (toy_problem_2(x0, x1 + h) - toy_problem_2(x0, x1 - h)) / (2 * h)
    else:
        gradient_x = (toy_problem_3(x0 + h, x1) - toy_problem_3(x0 - h, x1)) / (2 * h)
        gradient_y = (toy_problem_3(x0, x1 + h) - toy_problem_3(x0, x1 - h)) / (2 * h)

    grad[0][0] = gradient_x
    grad[1][0] = gradient_y
    return grad

def Hessian(x_pre, x, gk_pre, gk, Hk_pre):
    sk = x - x_pre
    yk = gk - gk_pre
    v = sk - np.dot(Hk_pre, yk)
    hess = Hk_pre + np.dot(v, v.T) / np.dot(v.T, yk)

    return hess

def CalculateOptimizedValue(pro, x):
    if pro == 0:
        zz = toy_problem_0(x[0][0], x[1][0])
    elif pro == 1:
        zz = toy_problem_1(x[0][0], x[1][0])
    elif pro == 2:
        zz = toy_problem_2(x[0][0], x[1][0])
    else:
        zz = toy_problem_3(x[0][0], x[1][0])
    return zz

def QuasiNewton(pro, x):
    tolerance = 1e-10
    iteration = 1000
    itera = 0
    z_pre = 0

    if pro == 0:
        z_task3_0.append(CalculateOptimizedValue(pro, x))
    elif pro == 1:
        z_task3_1.append(CalculateOptimizedValue(pro, x))
    elif pro == 2:
        z_task3_2.append(CalculateOptimizedValue(pro, x))
    else:
        z_task3_3.append(CalculateOptimizedValue(pro, x))

    Hk = np.eye(2)
    gk = FirstGrad(pro, x[0][0], x[1][0])

    dk = -1.0 * np.dot(Hk, gk)
    x_pre = x
    step = StepSearch(pro, x, gk, Hk)
    x = x + step * dk
    z_best = CalculateOptimizedValue(pro, x)

    if pro == 0:
        z_task3_0.append(z_best)
    elif pro == 1:
        z_task3_1.append(z_best)
    elif pro == 2:
        z_task3_2.append(z_best)
    else:
        z_task3_3.append(z_best)

    while (itera < iteration) and (abs(z_best - z_pre) > tolerance):
        Hk_pre = Hk
        gk_pre = gk
        gk = FirstGrad(pro, x[0][0], x[1][0])
        Hk = Hessian(x_pre, x, gk_pre, gk, Hk_pre)
        dk = -1.0 * np.dot(Hk, gk)
        x_pre = x
        step = StepSearch(pro, x, gk, Hk)
        x = x + step * dk
        z_pre = z_best
        z_best = CalculateOptimizedValue(pro, x)

        if pro == 0:
            z_task3_0.append(z_best)
        elif pro == 1:
            z_task3_1.append(z_best)
        elif pro == 2:
            z_task3_2.append(z_best)
        else:
            z_task3_3.append(z_best)

        itera += 1

    return x


# Main
problem = 4
z_task3_0 = []
z_task3_1 = []
z_task3_2 = []
z_task3_3 = []

for i in range(problem):
    x = np.zeros((2, 1))
    x[0][0] = 15
    x[1][0] = 15
    x_best = QuasiNewton(i, x)

    z_best = CalculateOptimizedValue(i, x_best)

    print("This is toy problem %d" % (i))
    print("x = %f, y = %f, Optimized value = %f" % (float(x_best[0][0]), float(x_best[1][0]), float(z_best)))