# Faça um Programa que leia três números e mostre o maior deles.

print('•------» Qual o maior? «------•')

num1 = int(input('Primeiro -> '))
num2 = int(input('Segundo -> '))
num3 = int(input('Terceiro -> '))

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O maior numero digitado é {maior}')

'''

Tentei fazer com if, elif, else:
    mas não tem como usar else como condição, apenas como decreto. 
    Exemplo: se não foi esse (if) talvez seja esse(elif), nenhum dos dois? entao é else!

'''