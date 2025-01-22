"""
#Estamos de volta pythonnnnnnnnnnnnnnnnn
num1=float(input("\nDigite o primeiro numero para soma:"))
num2=float(input("\nDigite o segundo numero: "))
soma=num1+num2
print(f"\nA soma da sua conta é: {soma}")

#Soma com numero int
num1=int(input("\nDigite o primeiro numero para soma:"))
num2=int(input("\nDigite o segundo numero: "))
soma=num1+num2
print(f"\nA soma da sua conta é: {soma}")

#str
frase=input("\nDigite uma frase motivadora: ")
adicao= frase + ".Não desista"
print(f"{adicao}")

#Nome,idade
nome=input("\nDigite seu nome : ")
ano=int(input("\nDigite seu ano de nascimento: "))
idade=  2025 -ano
print(f"{nome} , {idade} anos ")

#media

contador = 0
notas = []
while contador < 5:
    nota = float(input(f"Digite a nota {contador + 1}: "))
    notas.append(nota)
    contador += 1

media = sum(notas) / len(notas)
if media >= 5:
    print("Aluno Aprovado!")
elif media >2.5 <5:
    print("Aluno em Recuperação!")
else:
    print("Aluno Reprovado!")

#loop1
numero = int(input("Digite um número inteiro positivo: "))

if numero >= 0:
    for i in range(numero + 1):
        print(i)
else:
    print("Por favor, insira um número inteiro positivo.")

#loop2
maior = None

while True:
    numero = int(input("\nDigite um número (digite um número negativo para parar): "))
    if numero < 0:
        break
    if maior is None or numero > maior:
        maior = numero

if maior is not None:
    print(f"\nO maior número digitado foi: {maior}")
else:
    print("\nNenhum número positivo foi digitado.")

#função de inverter strings
def string_invertida(s):
    string_invertida=""
    for i in range(len(s)-1,-1,-1):
        string_invertida+=s[i]
    return string_invertida
string_original=input("\nDigite uma palavra: ")
resultado=string_invertida(string_original)

print((f"\nA string original é {string_original} e a invertida é \n{resultado}"))
"""


def contar_caracteres(s):
    contagem = {}
    for i in s:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
    return contagem
print(contar_caracteres("banana"))




