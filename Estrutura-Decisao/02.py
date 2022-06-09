# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print('◦•● Negativo ou Positivo? ●•◦')

num = int(input('Digite o numero -> '))

if num == 0:
    print(num,'é neutro.')

elif num >= 1:
    print(num,'é positivo.')
else:
    print(num, 'é negativo.')