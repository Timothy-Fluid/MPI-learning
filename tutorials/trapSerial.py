import numpy as np
import sys
import time

# command line input
a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])


def f(x):
    return x**2


def integrate(a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    x_i = np.linspace(a, b, n + 1)
    for x in x_i[1:n]:
        integral = integral + f(x)
    return integral * h


begin = time.time()
integral = integrate(a, b, n)
end = time.time()
print("With n = " + str(n) + "trapezoids, the estimate of the integral from a = " +
      str(a) + " b = " + str(b) + " is " + str(integral))
print("Time taken " + str(end - begin))
