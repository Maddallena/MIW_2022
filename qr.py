import numpy as np
import math

np.set_printoptions(suppress=True)

def projekcja(u, v):
    return (np.dot(u, v) / np.dot(u, u)) * u


def normalizacja(u):
    return u / math.sqrt(np.dot(u, u))


def dekompozycja(macierz):
    A = macierz.T
    vectors_list = []
    u = []
    norm = []
    for col in range(len(A) - 1):
        vectors_list.append(A[:, col])
    u.append(vectors_list[0])
    for i in range(1, len(vectors_list)):
        for j in range(i):
            vectors_list[i] = vectors_list[i] - projekcja(u[j], vectors_list[i])
            u.append(vectors_list[i])
    for e in range(len(u)):
        w = normalizacja(u[e])
        norm.append(w)

    QT = np.vstack(norm)#dostaję od razu macierz "transponowaną" bo łączę dwie listy
    Q = QT.T
    R = QT @ A

    return Q, R


arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr)
Al = arr.T
print(Al[:, 0])
print(Al[:, 1])
print(Al[:, 2])
print(Al)

arrr = np.array([[2, 1, 0], [0, 1, 2]])

a, b = dekompozycja(arrr)

print(f'{a}\n{b}')

