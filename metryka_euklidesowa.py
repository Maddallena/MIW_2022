import math
import numpy as np


lista_australian = []


with open('australian.dat', 'r') as file:
    for line in file:
        kolekcja = line.replace('\n', '').split()
        result = list(map(lambda e: float(e), kolekcja))
        lista_australian.append(result)


def MetrykaEuklidesowa(listaA, listaB):

    dl = len(listaA) - 1
    tmp = 0
    for id in range(dl):
        zm1 = listaA[id]
        zm2 = listaB[id]
        c = zm1 - zm2
        wynik = c ** 2
        tmp += wynik

    result = math.sqrt(tmp)

    return result


def Distance(lista):

    y = lista[0]
    s = {}

    for l in range(len(lista))[1:]:
        tmpl = lista[l]
        ost = len(tmpl) - 1
        key = int(tmpl[ost])
        wynik = MetrykaEuklidesowa(y, lista[l])
        if key not in s:
            s[key] = []
            s[key].append(wynik)
        else:
            s[key].append(wynik)
            # print(f'Odległość listy {l} od y wynosi: {wynik}')
    return s


def MetrykaEuklidesowa2(lista1, lista2):

    li1 = lista1[:-1] #nie bierze pod uwagę ostatniego elementu, żeby można było zastosować to też do australian.dat
    li2 = lista2[:-1]

    v1 = np.array(li1)
    v2 = np.array(li2)

    c = v1 - v2

    il_skalarny = np.dot(c, c)
    result = math.sqrt(il_skalarny)

    return result


w = Distance(lista_australian)
for e in w:
    print(f'klucz: {e}, wartość: {w[e]}\n')


l1 = [1, 2, 3]
l2 = [3, 4, 6]

M1 = MetrykaEuklidesowa(l1, l2)
print(f'M1: {M1}')

M2 = MetrykaEuklidesowa2(l1, l2)
print(f'M2: {M2}')