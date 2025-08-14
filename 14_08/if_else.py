nota = float(input("Digite a primeira nota: "))
nota1 = float(input("Digite a segunda nota: "))

media = (nota + nota1) / 2

if(media >= 6):
    print("Aprovado. Média: ", media)
elif(media >= 5):
    print("Recuperação")
else:
    print("Reprovado. Média: ", media)

'''
text = "oiii 72"
print(text.isalnum()) # Detecta se a String é apenas um número
'''