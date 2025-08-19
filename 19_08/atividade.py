# 1 - Crie uma lista que contenha diferentes tipos de dados

# lista = ["Lista", 1, 0, 9936.76, [1, 2, 3]]
# print(lista)


# 2 - Usando a lista criada na questão anterior, use o método insert ou append para
# adicionar mais dois elementos a lista e use remove, pop ou del para remover um
# elemento da lista.

#lista.append("Carro")
# print(lista)

# lista.remove("Lista")
# print(lista)


# 3 - Faça uma cópia da lista da questão anterior. Use a função id para verificar se
# realmente criou uma lista nova (obs: mesmo valor de ID indica que é o mesma lista
# e não uma nova)

#lista1 = lista.copy()

# print(id(lista))
# print(id(lista1))

# 4 -  Crie uma nova lista só com números (inteiro e/ou ponto flutuante) e multiplique os
# elementos da lista por 5. O resultado deve ser uma nova lista com os elementos
# multiplicados
'''
lista = [1, 2, 3, 4, 5]
lista1 = []

for i in lista:
    num = i * 5
    lista1.append(num)

print(lista1)
'''


# 5 -  Use o slice para criar uma nova lista que inclua apenas os elementos com índice
# 3 e 4 da lista a seguir:
# [ 1,2,3,4,5,6 ]

lista = [1, 2, 3, 4, 5, 6]

lista1 = lista[3:4]

print(lista)
print(lista1)