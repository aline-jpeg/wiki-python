'''
Faça um Programa que peça 2 números inteiros e um número real. 

    Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''


print('------ INTEIROS E REAL ------')
print('')


num1 = int(input('Numero inteiro: '))
num2 = int(input('Outro numero inteiro: '))
num3 = float(input('Numero real: '))

print ('Soma:', ((2*num1) * (num2/2)))
print ('Produto:', (3 * num1) + num3)
print ('Cubo:', num3**3)