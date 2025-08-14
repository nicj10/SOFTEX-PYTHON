# 1 - Par ou impar
'''
num = int(input('Digite um número: '))
if (num % 2) == 0: print("PAR")
else: print("ÍMPAR")
'''

# 2 - Aprovação escolar
'''
nota = float(input('Digite a nota do aluno: '))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
'''

# 3 - Comparação de números
'''
num = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num > num2:
    print(f"{num} é maior que {num2}")
elif(num == num2):
    print("São iguais")
else:
    print(f"{num2} é maior que {num}")
'''

# 4 - Idade
'''
idade = int(input("Digite sua idade: "))

def faixa_etaria(idade):
    if(idade <= 12):
        return "Criança"
    elif(idade <= 17):
        return "Adolescente"
    elif(idade <= 64):
        return "Adulto"
    else:
        return "Idoso"
    
print(faixa_etaria(idade))
'''


#### LAÇOS FOR E WHILE ####
# 1 - Contagem crescente  
''''
for i in range(1, 11):
    print(i)
'''

# 2 - Tabuada do número
'''
num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
'''
# 3 - Somatória
'''
n = float(input("Digite o número: "))
soma = 0

while(n !=0):
    soma += n
    n = float(input("Digite outro número: "))

print(soma)
'''
### FUNÇOES ###
# 1 - Função de saudação
'''
nome = input("Digite seu nome: ")
def saudacao(nome):
    print(f"Olá, {nome}")

print(saudacao(nome))
'''
# 2 - Calculadora
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("SELECIONE A OPERAÇÃO: "))


def calculadora(operacao):
    match operacao:
        case 1:
            return a + b;
        case 2:
            return a - b;
        case 3:
            return a * b;
        case 4:
            return a / b;

print(calculadora(operacao))

