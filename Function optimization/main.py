import numpy as np # importing numpy as symbolic np in order to use those functions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def toy_problem_0(x, y):
    w1= 0.3
    w2 = 0.3
    # to prevent any integer issues
    x = np.array(x)
    y = np.array(y)
    # if only one value is provided (pointwise)
    if x.shape == () and y.shape == ():
        z = x**2 + y**2
        return z
    # else we are dealing with an array of values, as for example plotting or maybe a population
    else:
        len_x = x.shape[0]
        len_y = y.shape[0]
        z = np.zeros([len_x, len_y])
        for _x in range(len_x):
            for _y in range(len_y):
                z[_x, _y] = x[_x]**2 + y[_y]**2
        return z

def toy_problem_1(x, y):
    w1= 0.3
    w2 = 0.3
    # to prevent any integer issues
    x = np.array(x)
    y = np.array(y)
    # if only one value is provided
    if x.shape == () and y.shape == ():
        z = np.sqrt(x**2 + y**2)
        return z
    # else we are dealing with an array of values, so let's do that
    else:
        len_x = x.shape[0]
        len_y = y.shape[0]
        z = np.zeros([len_x, len_y])
        for _x in range(len_x):
            for _y in range(len_y):
                z[_x, _y] = np.sqrt(x[_x]**2 + y[_y]**2)
        return z

def toy_problem_2(x, y):
    w1= 0.45
    w2 = 0.5
    x = np.array(x)
    y = np.array(y)
    if x.shape == () and y.shape == ():
        case1 = np.sqrt(x**2 + y**2)-np.pi/(w1*w2)
        case2 =(np.sqrt(x**2 + y**2)-np.pi/(w1*w2))*np.cos(w1*w2*np.sqrt(x**2 + y**2))
        if case1 >= 0:
            z = case1
        else:
            z = case2
        return z
    else:
        len_x = x.shape[0]
        len_y = y.shape[0]
        z = np.zeros([len_x, len_y])
        for _x in range(len_x):
            for _y in range(len_y):
                case1 = np.sqrt(x[_x]**2 + y[_y]**2)-np.pi/(w1*w2)
                case2 =(np.sqrt(x[_x]**2 + y[_y]**2)-np.pi/(w1*w2))*np.cos(w1*w2*np.sqrt(x[_x]**2 + y[_y]**2))
                if case1 >= 0:
                    z[_x, _y] = case1
                else:
                    z[_x, _y] = case2
        return z

def toy_problem_3(x, y):
    w1= 0.45
    w2 = 0.5
    x = np.array(x)
    y = np.array(y)
    if x.shape == () and y.shape == ():
        z = np.sqrt(x**2 + y**2) - 1/(w1*w2)*np.cos(w1*x)*np.cos(w2*y)
        return z
    else:
        len_x = x.shape[0]
        len_y = y.shape[0]
        z = np.zeros([len_x, len_y])
        for _x in range(len_x):
            for _y in range(len_y):
                z[_x, _y] = np.sqrt(x[_x]**2 + y[_y]**2) - 1/(w1*w2)*np.cos(w1*x[_x])*np.cos(w2*y[_y])
    return z



if __name__ == "__main__":
    # how many steps and at what resolution do I want to plot
    steps = 350
    x = 0.1*np.arange(-steps/2, steps/2)
    y = 0.1*np.arange(-steps/2, steps/2)
    X, Y = np.meshgrid(x, y)

    # defining the figure parameters
    fig = plt.figure(figsize=(15,20))

    # first subplot of four
    ax1 = fig.add_subplot(411, projection='3d')
    surf1 = ax1.plot_surface(X, Y, toy_problem_0(x, y),
                            cmap=cm.coolwarm,
                            linewidth=0,
                            antialiased=False)
    ax1.set_xlabel('X axis')
    ax1.set_ylabel('Y axis')
    ax1.set_zlabel('Z axis')
    ax1.set_title('Problem 0 surface')
    fig.colorbar(surf1, shrink=0.4, aspect=5, label='Z-Axis values')

    # second subplot of four
    ax2 = fig.add_subplot(412, projection='3d')
    surf2 = ax2.plot_surface(X, Y, toy_problem_1(x, y),
                            cmap=cm.coolwarm,
                            inewidth=0,
                            ntialiased=False)
    fig.colorbar(surf2,  shrink=0.4, aspect=5, label='Z-Axis values')
    ax2.set_xlabel('X axis')
    ax2.set_ylabel('Y axis')
    ax2.set_zlabel('Z axis')
    ax2.set_title('Problem 1 surface')

    # third subplot of four
    ax3 = fig.add_subplot(413, projection='3d')
    surf3 = ax3.plot_surface(X, Y, toy_problem_2(x, y),
                            cmap=cm.coolwarm,
                            linewidth=0,
                            antialiased=False)
    fig.colorbar(surf3, shrink=0.4, aspect=5, label='Z-Axis values')
    ax3.set_xlabel('X axis')
    ax3.set_ylabel('Y axis')
    ax3.set_zlabel('Z axis')
    ax3.set_title('Problem 2 surface')

    # fourth subplot of four
    ax4 = fig.add_subplot(414, projection='3d')
    surf4 = ax4.plot_surface(X, Y, toy_problem_3(x, y),
                            cmap=cm.coolwarm,
                            linewidth=0,
                            antialiased=False)
    fig.colorbar(surf3, shrink=0.4, aspect=5, label='Z-Axis values')
    ax4.set_xlabel('X axis')
    ax4.set_ylabel('Y axis')
    ax4.set_zlabel('Z axis')
    ax4.set_title('Problem 3 surface')

    # and show plots
    plt.show()