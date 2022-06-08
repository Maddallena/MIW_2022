import numpy as np

def DetDwa(m):
    result = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return result

def DetTrzy(m):
    result = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] \
             - m[2][0] * m[1][1] * m[0][2] - m[2][1] * m[1][2] * m[0][0] - m[2][2] * m[1][0] * m[0][1]
    return result

# Próba samodzielnego napisania, ale nie umiałam zrobić dobrze rekurencji
# def ObliczWyznacznik(v, c, r):
#
#     if c == r:
#         m = np.array(v).reshape(c, r)
#         print(f'Twoja macierz to:\n{m}')
#         if c == 2:
#             w = DetDwa(m)
#             print(w)
#         elif c == 3:
#             w = DetTrzy(m)
#             print(w)
#         # else:
#     else:
#         print('Nie można wyliczyć wyznacznika.')

#
# def wyznacznik(A, calosc=0):
#     indeksy = list(range(len(A)))
#
#     if len(A) == 2 and len(A[0]) == 2:
#         return DetDwa(A)
#
#     for kolumna in indeksy:
#         kopiaA = np.copy(A)
#         kopiaA = kopiaA[1:]
#         il_rzedow = len(kopiaA)
#         for i in range(il_rzedow):
#             kopiaA[i] = kopiaA[i][0:kolumna] + kopiaA[i][kolumna+1:]
#
#         znak_jedynki = (-1) ** (kolumna % 2)
#         niecaly_wyznacznik = wyznacznik(kopiaA)
#         calosc += znak_jedynki * A[0][kolumna] * niecaly_wyznacznik
#     return calosc

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# npDet = np.linalg.det(A)
# det = wyznacznik(A)
# print(npDet)
# print(det)


def malamacierz(m, i, j):
    return[row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]
# wykluczamy rząd i i kolumnę j


def wyznacznik_kolejna_wersja(matrix):
    if(len(matrix) == 2):
        return DetDwa(matrix)
    suma = 0

    for kolumna in range(len(matrix)):
        znak = (-1) ** (kolumna)

        maly_wyznacznik = wyznacznik_kolejna_wersja((malamacierz(matrix, 0, kolumna)))

        suma += (znak * matrix[0][kolumna]*maly_wyznacznik)

    return suma


mat = [[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]]

A = [[-2,2,-3],[-1,1,3],[2,0,-1]]

mat2 = [[4, 2, -5, 8],
           [1, 1, -2,0],
           [4, 0, 0, 0],
           [3, -1,-2, 4]]


print(wyznacznik_kolejna_wersja(mat))
print(wyznacznik_kolejna_wersja(mat2))
print(wyznacznik_kolejna_wersja(A))