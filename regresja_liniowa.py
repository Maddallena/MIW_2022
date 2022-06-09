import numpy as np

def regresja_liniowa(x, y):
    list_of_1 = [1 for i in range(len(x))]
    c = np.array([list_of_1, x]).T
    cT = c.T
    step1 = cT @ c
    step2 = np.linalg.inv(step1)
    step3 = step2 @ cT @ y
    return step3


a = [1,5,6,9]
b = [3,6,7,8]

print(regresja_liniowa(a,b))
