'''
Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 

O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: 
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: 
Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

print('----- CAIXA ELETRONICO -----')
print('')
print('Digite o valor desejado:')
valor = int(input('R$ '))

if valor < 10 or valor > 600:
    print('Valor invalido, tente novamente.')
else:
    cem = int (valor / 100)
    valor = valor - (cem * 100)
    cinquenta = int(valor / 50)
    valor = valor - (cinquenta * 50)
    dez = int (valor / 10)
    valor = valor - (dez * 10)
    cinco = int (valor / 5)
    valor = valor - (cinco * 5)
    um = valor

print('')
print('Você vai precisar de:')
print(f'{cem} - nota(s) de cem')
print(f'{cinquenta} - nota(s) de cinquenta')
print(f'{dez} - nota(s) de dez')
print(f'{cinco} - nota(s) de cinco')
print(f'{um} - nota(s) de um')