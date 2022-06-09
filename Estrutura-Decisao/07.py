# Faça um Programa que leia três números e mostre o maior e o menor deles.

print('•------» Maior & Menor «------•')

num1 = int(input('Primeiro -> '))
num2 = int(input('Segundo -> '))
num3 = int(input('Terceiro -> '))

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
    menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3

print(f'O maior é {maior} e o menor é {menor}')