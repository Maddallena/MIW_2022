import numpy as np
import math


def srednia(vec):
    sred = sum(vec)/len(vec)
    return sred


def wariancja(vec):
    res = sum((x - srednia(vec))**2 for x in vec)/len(vec)
    return res


def odchylenie_standardowe(vec):
    war = wariancja(vec)
    res = math.sqrt(war)
    return res

v = np.array([1,2,3])

print(srednia(v))
print(wariancja(v))
print(odchylenie_standardowe(v))