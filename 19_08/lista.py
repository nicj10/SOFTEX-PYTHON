# Vamo ver lista
'''
lista = []
print(type(lista))


frutas = ["maçã", "banana", "uva", "salada", "abóbora", "manga", "salada mista"]
frutas.append("laranja")
frutas.insert(0, "pera")
frutas.extend(["jaca", "mamão"])

frutas.remove("banana")
frutas.pop(0)
print(frutas)

del frutas[5]
print(frutas)
'''

lista = [1, 2, 3, 4, 5, 6]

lista2 = lista[:]

lista3 = lista.copy()

# print(id(lista))
# print(id(lista2))
# print(id(lista3))

# lista.clear()

# print(lista.index(5))
lista.sort()
lista.reverse()
print(lista)


