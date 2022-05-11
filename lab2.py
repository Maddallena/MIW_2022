# panstwa_stolice = {
#     'Rosja': 'Moskwa',
#     'Litwa': 'Wilno',
#     'Białoruś': 'Mińsk',
#     'Ukraina': 'Kijów',
#     'Słowacja': 'Bratysława',
#     'Czechy': 'Praga',
#     'Niemcy': 'Berlin',
# }
# print(panstwa_stolice.keys())
# print(panstwa_stolice.values())
# panstwa_stolice['Hiszpania'] = 'Madryt'
# print(panstwa_stolice)

# jak posortować do domu

# print(bool(""))
# print(bool(" "))
# print(bool(0))
# print(bool(1))
# print(bool('0'))
# print(bool('1'))
# print(bool([]))
# print(bool([',']))

napis = 'Metody inzynierii wiedzy'

print('s' in napis)

for n in range(21):
    print(n)

# for litera in napis:
#     print(litera)

# nowa_lista = ["head", "shoulders", "knees", "and", "toes"]
#
# # print(nowa_lista)
kolejna = []
# for el in nowa_lista:
#     kolejna.append(el)
#

nowa_lista = ["head", "shoulders", "knees", "and", "toes"]
zdanie2 = "-".join(nowa_lista)
print(zdanie2)
s = ''
for z in zdanie2:
    if z != '-':
        s += z
    else:
        kolejna.append(s)
        s = ''
kolejna.append(s)
print(kolejna)

# podzielic = zdanie2.split("-")
# print(podzielic)

def silneHaslo(haslo):

    silne = False
    rozne = True

    if haslo.isupper() or haslo.islower():
        rozne = False

    if len(haslo) >= 10 and rozne == True and '!' in haslo:
        silne = True

    return silne

h = "magdalena"
h1 = 'magdalena100'
h2 = 'magDalena100'
h3 = 'magDalena100!'
print(silneHaslo(h))
print(silneHaslo(h1))
print(silneHaslo(h2))
print(silneHaslo(h3))

