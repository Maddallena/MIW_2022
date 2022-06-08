import math
import random

import numpy as np


#australian = []
#with open('australian.dat', 'r') as file:
#    for line in file:
#        kolekcja = line.replace('\n', '').split()
#        result = list(map(lambda e: float(e), kolekcja))
#        australian.append(result)

losowe = []
with open('losowedane2.dat', 'r') as file:
   for line in file:
       kolekcja = line.replace('\n', '').split()
       result = list(map(lambda e: float(e), kolekcja))
       losowe.append(result)

# liczenie odległości elementów metryki od siebie by poznać odległość jednej listy od drugiej
def MetrykaEuklidesowa(listaA, listaB):

    dl = len(listaA)
    tmp = 0

    for id in range(dl):
        zm1 = listaA[id]
        zm2 = listaB[id]
        c = zm1 - zm2
        wynik = c ** 2
        tmp += wynik

    result = math.sqrt(tmp)

    return result

# funkcja tworzy słownik z listy list np. australiana.dat,
# kluczem jest indeks danej listy, a wartością jest jej odległość od kolejnych list
# odległość listy samej od siebie też występuje na odpowiednim indeksie i wynosi 0
def odleglosc(lista_list):

    s = {}

    for i in range(len(lista_list)):
        key = i
        for j in range(len(lista_list)):
            l1 = lista_list[i]
            l2 = lista_list[j]
            res = MetrykaEuklidesowa(l1, l2)

            if key not in s:
                s[key] = []
                s[key].append(res)
            else:
                s[key].append(res)
    return s

# 1. Randomowo nadajesz klasy decyzyjne
# Funkcja przy wywołaniu przyjmuje jako parametry listę list oraz ile klas ma zostać randomowo nadanych listom
# Randomowo nadana klasa znajduje się potem na końcu listy, która jest w pętli o tę klasę rozszerzana

def randomowe_klasy(lista, ilosc_klas):

    for l in range(len(lista)):
        klasa = random.randrange(ilosc_klas+1)
        lista[l][-1] = klasa
    return lista


# 2. Dzielisz wiersze na grupy po klasach decyzyjnych.
# Funkcja przyjmuje listę list, które mają już nadane randomowo klasy (które są ostatnim elementem

# sortuje je według tych klas - kluczem jest klasa a wartość to lista list, które mu odpowiadają

def podzial_wierszy(lista):

    grupy = {}

    for el in lista:
        key = el[-1]
        wartosc = el

        if key not in grupy:
            grupy[key] = []
            grupy[key].append(wartosc)
        else:
            grupy[key].append(wartosc)
    return grupy



# 3. W każdej grupie bierzesz każdy wiersz i liczysz sumę odległości do każdego wiersza.
# Funkcja przyjmuje słownik, po czym dla każdego klucza liczy sumę elementów,
# a następnie zamienia dla każdego klucza wartość, z listy odległości na ich sumę.
# Funkcja ta jest potem użyta w kolejnej.
def sumaodl(slownik):
    suma = 0
    for key in slownik:
        lista_wartosci = slownik[key]
        for el in lista_wartosci:
            suma += el
            slownik[key] = suma
        suma = 0
    return slownik



# Funkcja przjmuje słownik z pogrupowanymi listami według ich klasy.
# Następnie tworzy słownik, który będzie słownikiem słowników.
# Pętla iteruje po kluczach w słowniku pogrupowane, a za listę wartości przyjmuje listę list,
# która jest odpowiednia dla danego klucza.
# Następnie tworzy słownik odległości, w którym kluczem jest indeks każdego elementu w liście list,
# a wartości to odległości od pozostałych elementów - do tego użyta zostaje funkcja odleglosc.
# Na tym etapie do słownika słowników, w którym główne klucze są takie same jak w słowniku pogrupowane,
# dodawane są słowniki powstałe przez użycie funkcji odległość.

# Kolejna pętla iteruje po słowniku słowników, która liczy dla wewntętrznych słowników odległości,
# sumy tej odległości od każdego wiersza i zamienia je jako wartości dla danych klas w słowniku nested_dict.


def suma_odleglosci_od_wierszy(pogrupowane):
    nested_dict = {}

    for key in pogrupowane:
        lista_wartosci = pogrupowane[key]
        odl = odleglosc(lista_wartosci)
        nested_dict[key] = odl
    for k in nested_dict:
        wynik = sumaodl(nested_dict[k])
        nested_dict[k] = wynik
    return nested_dict



# 4. Gdy masz już te odległości, szukasz wiersza który, ma najmniejsza sumę.
# Otrzymujesz w tym przypadku (australian.dat) dwa minima (jedno dla klasy 0, drugie dla 1).

# Przyjmuje dwa słowniki, tworzy słownik minimum
# Iteruje przez słownik słowników, czyli nested_dict z poprzedniej funkcji
# i przy użyciu lambdy szuka minimalnej wartości, czyli najmniejszej sumy, ale zwraca odpowiadający jej klucz,
# który jest indeksem listy, dzieki czemu otrzymujemy słownik,
# w którym dla każdej klasy mamy indeks listy z najmniejszą odległością do wszystkich pozostałych w danej klasie.
# Następnie w słowniku min_v wartość dla każdego z klucza (klucz to randomowo wcześniej nadana klasa)
# zostaje zamieniona na odpowiednią listę ze słownika list,
# która ma w danej klasie najmniejszą odległość do pozostałych list.

def znajdz_minimum(slownik_slownikow, slownik_list):
    min_v = {}
    for klasa in slownik_slownikow:
        min_value = min(slownik_slownikow[klasa],
                        key=lambda dict_key: slownik_slownikow[klasa][dict_key])
        min_v[klasa] = min_value
        min_v[klasa] = slownik_list[klasa][min_v[klasa]]
    return min_v

# 5. Dla KAŻDEGO wiersza liczysz odległość do minima z grupy 1 i odległość do minimum z grupy 0.
# Jeżeli randomowo przydzielona klasa to 1 a odległość do 0 jest mniejsza, zmieniasz na 0.

# Z listy list, w ktorej klasy zostały randomowo nadane tworzony jest słownik, w którym kluczami są indeksy danych list.
# slownik_minimum, to słownik, który utworzyła poprzednia funkcja.
# Iterujemy po slowniku minimów według klucza,
# wartości ze słownika minimów podstawiamy pod zmienną mini_mini
# liczymy odległości każdej listy z listy list od minimum
# do słownika "odleglosci_do_porownania" jest dodana najmniejsza odległość w każdej z klas
# więc np. odległosc_od_porownania[indeks_listy][klasa] = odleglość tej listy od minimum w tej klasie
# potem wybieramy najmniejszą odległość i jest zwracany słownik,
# w którym dla każdego indeksu listy z listy_list jest okreslona klasa,
# do której jest danej liście bliżej.

def blizsza_klasa(lista_list, slownik_minimum):
    min_v = {}
    odleglosci_do_porownania = {}
    for el in range(len(lista_list)):
        odleglosci_do_porownania[el] = {}
        for key in slownik_minimum:
            mini_mini = slownik_minimum[key]
            odl_od_minimum = MetrykaEuklidesowa(mini_mini, lista_list[el])
            odleglosci_do_porownania[el][key] = odl_od_minimum
        for k in odleglosci_do_porownania:
            min_value = min(odleglosci_do_porownania[k],
                            key=lambda dict_key: odleglosci_do_porownania[k][dict_key])
            min_v[k] = min_value
    return min_v



# Funkcja przyjmuje liste_list z randomowo nadanymi klasami
# i słownik, w którym klucz to indeks listy na liscie_list
# a wartość to klasa, do której tej liście jest bliżej
# Tworzona jest nowa lista list, która przyjmuje listy z nowymi klasami,
# ale jest to stworzone w ten sposób by móc porównywać wcześniejszą listę z nową listą i
# w kolejnym etapie wyszukiwać różnice,
# na podstawie których będzie wiadomo czy nalezy zakończyć program.

def nowa_klasa(lista_list, slownik_blizszych_klas):
    nowa_lista = []
    for klucz in slownik_blizszych_klas:
        lista = lista_list[klucz]
        lista[-1] = slownik_blizszych_klas[klucz]
        nowa_lista.append(lista)
        #lista_list[klucz] = lista
    return nowa_lista


def centra_masy(lista_list):
    lista_z_klasami = randomowe_klasy(lista_list, 3)
    for l in lista_z_klasami:
        print(l)

    zmiana = True
    while zmiana:
        slownik_klas = podzial_wierszy(lista_z_klasami)
        suma_odl = suma_odleglosci_od_wierszy(slownik_klas)
        znalezione_min = znajdz_minimum(suma_odl, slownik_klas)
        co_blizej = blizsza_klasa(lista_z_klasami, znalezione_min)
        kolejny_podzial = nowa_klasa(lista_z_klasami, co_blizej)

        for el in range(len(lista_z_klasami)):
            if lista_z_klasami[el][-1] != kolejny_podzial[el][-1]:
                zmiana = True
            else:
                zmiana = False

    return kolejny_podzial




print('\n')

knn = centra_masy(losowe)
print('\nknn:\n')
for n in knn:
    print(n)