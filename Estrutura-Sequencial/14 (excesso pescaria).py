'''
O pescador João, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 

Imprima os dados do programa com as mensagens adequadas.

'''

print('------ PESCARIA ------')
print('')


peso = float(input('Digite o peso (peixe) ->'))
valorPermitido = 50.00

if peso > valorPermitido:
    excesso = peso - 50
    multa = excesso * 4.00
    print('Você tem ''{:.1f}'' Kgs em excesso'.format(excesso),'. Sua multa será de -> R$''{:.2f}'.format(multa))
else:
    print('Valores dentro do regulamento de pesca do estado de São Paulo.')