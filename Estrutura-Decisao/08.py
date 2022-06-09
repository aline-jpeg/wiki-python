# Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

print('•------» Produto mais barato «------•')

preco1 = float(input('Preço 1: '))
preco2 = float(input('Preço 2: '))
preco3 = float(input('Preço 3: '))

menor = preco1

if preco2 < preco1 and preco2 < preco3:
    menor = preco2
if preco3 < preco1 and preco3 < preco2:
    menor = preco3

print(f'O mais barato é: {menor}')