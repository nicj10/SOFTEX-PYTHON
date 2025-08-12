from datetime import date
# PESQUISEI COMO USAR A BIBLIOTECA PARA CALCULAR A IDADE EM DIAS DE FORMA EXATA
# Atividade de Python Básico - Softex

# 1 - Primeira mensagem
# print("Olá mundo")

# 2 - Mensagens múltiplas
"""
print("Olá mundo")
print("Olá Softex")
print("Olá Phyton")
"""

# 3 -  Texto com quebra de linha e tabulação
"""print("Nome: João")
print("Idade: 20 anos")
print("Curso: Python básico")
"""
# 4 -  Combinar textos e números
"""
nome = "João"
idade = 20
curso = "Python Básico"

print(f"{nome} tem {idade} anos e está cursando {curso}.")
"""
# 5 - Desenho com caracteres
"""
print("# # #")
print("#   #")
print("#   #")
print("# # #")
"""
# 6 - Operações básicas
"""
a = 10
b = 3

print(a + b)
print( a - b)
print( a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
"""
# 7 - Calculadora simples
"""
num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print(f"Soma: {num + num2}")
print(f"Subtração: {num - num2}")
print(f"Multiplicação: {num * num2}")
print(f"Divisão: {num // num2 if num2 != 0 else 'Divisão por zero não é permitida'}, resto da divisão: {num % num2 if num2 != 0 else 'Divisão por zero não é permitida'}")
"""
# 8 - Idade em dias
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_nascimento.split('/'))
data_atual = date.today()
idade_dias = (date(data_atual.year, data_atual.month, data_atual.day) - date(ano, mes, dia)).days
print(f"Sua idade em dias é: {idade_dias} dias")

# 9 - Área de um retângulo
"""
b = float(input("Digite o valor da base do retângulo: "))
h = float(input("Digite o valor da altura do retângulo: "))

print(f"A área do retângulo é: {int(b * h)} m²")
"""
# 10 - Desafio do troco
'''
valor = float(input("Digite o valor da compra: "))
pag = float(input("Digite o valor pago: "))

if(pag < valor):
    print("Valor pago é menor que o valor da compra.")
elif(pag == valor):
    print("Não há troco.")
else:
    troco = pag - valor
    print(f"Troco: {troco:.2f} reais")
'''