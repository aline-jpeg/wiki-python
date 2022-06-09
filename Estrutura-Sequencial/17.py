'''
Faça um Programa para uma loja de tintas. 

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 

Considere que a cobertura da tinta é: 
1 litro para cada 6 metros quadrados vendida em latas de 18 litros, que custam R$ 80,00 ou em 
galões de 3,6 litros, que custam R$ 25,00.

lata = 18 litros (108mt²) = 80 R$ || galão = 3.6 litros (21.6mt²) = 25 R$

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

import math


print('		░▒▓█ LOJA DE TINTAS █▓▒░\n')

area = int(input('Quantos mt² deseja pintar?\n'))

litros = (area / 6) * 1.1

latas = math.ceil(litros / 18)

precoLata = latas * 80

galao = math.ceil(litros / 3.6)

precoGalao = galao * 25

# --------- MISTURA DE LATAS

mixLatas = round(litros /18)
mixGaloes = round(litros - mixLatas * 18) / 3.6

if ((litros - (mixLatas * 18) % 3.6 != 0)): # ------ Resto da divisão (%) for diferente (!=) de 0.
    mixGaloes += 1
    totalMix = (mixLatas * 80) + (mixGaloes * 25)

print(f'Você vai precisar de: {latas} lata(s) ••• VALOR TOTAL: R$ {precoLata :.2f}')
print(f'Você vai precisar de: {galao} galão(ões) ••• VALOR TOTAL: R$ {precoGalao:.2f}')
print(f'Economize: {mixLatas} lata(s) & {mixGaloes :.0f} galão(ões) ••• VALOR TOTAL: R$ {totalMix :.2f}')