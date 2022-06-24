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

valor = int(input('Digite o valor entre 10 e 600. - '))

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
    print(f"Para R$ {valor} vai precisar de:\n{cem} - nota(s) de cem, \n{cinquenta} - nota(s) de cinquenta, \n{dez} - nota(s) de dez, \n{cinco} - nota(s) de cinco, \n{um} - nota(s) de um.")