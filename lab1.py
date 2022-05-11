# imie = input('Jak masz na imię?')
# zdanie = 'Cześć {}'.format(imie)
#
# print(zdanie)
# print(zdanie[-1])
# print(type(zdanie[2:3]))
# print(zdanie[2:])
# print(zdanie[:3])
# print(zdanie[::2])

a = 'metdinzwiedz'
b = 13
c = 13.5


print("typ zmiennej a: {}".format(type(a)))
print(type(b))
print(type(c))

nowa_lista = ["head", "shoulders", "knees", "and", "toes"]
zdanie2 = "-".join(nowa_lista)
print(zdanie2)
podzielic = zdanie2.split("-")
print(podzielic[2:])

aa = 'Metody Inżynierii Wiedzy są najlepsze.'
print("zdanie '{}' ma tyle znaków: {}".format(aa, len(aa)))
print(aa.lower())
print(aa.upper())
print(aa.capitalize())
bb = aa.replace("ż","z").replace("ą","a")
print("Zdanie '{}' ma tyle znaków: {}, a zdanie '{}', ma tyle: {}".format(aa, len(aa), bb, len(bb)))
new_set = set(bb)
print(new_set)
print(len(new_set))

x = "str"
y = 15
para = (x, y)
print(type(para))
liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
cc = liczby + litery
print(cc)

print(cc.index('e'))
# print(cc.index())
liczby.append('b')
# litery.extend()
# liczby.insert(litery[3])
# accounts
# sort, reverse
# przypomnieć sobie jak się liczy macierz odwrotną i kiedy można ją policzyć

