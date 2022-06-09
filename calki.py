import numpy as np
# o to ilość obserwacji w zakresie a,b

# def monte_carlo(o,a,b):
#     x = np.random.uniform(a,b,o)
#     f_x = x / ((1 + x) ** 3)
#     res = np.mean((f_x)*(b-a))
#     return res
#
#
# p = monte_carlo(10000000, 5, 20)
# print(p)


a = 0
b = np.pi #limit
N = 1000 #obserwacje
xrand = np.zeros(N)

for i in range(len(xrand)):
    xrand[i] = np.random.uniform(a,b)

def func(x):
    return np.sin(x)

integral = 0.0

for i in range(N):
    integral += func(xrand[i])

result = (b-a)/float(N)*integral


# można to na wykresie dac
areas = []

for i in range(N):
    xrand = np.zeros(N)

    for i in range(len(xrand)):
        xrand[i] = np.random.uniform(a,b)
        integral = 0.0

    for i in range(N):
        integral += func(xrand[i])

    wynik = (b-a)/float(N)*integral
    areas.append(wynik)

print(areas)
