'''
Faça um programa para uma loja de tintas. 

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    1 lata = 18l (18 * 3 = 54 mt²)
    1 lata = 54 mt²

'''
print('------ LOJA DE TINTAS ------')
print('')

tamanho = float(input('Digite o tamanho em mt²: '))

litros = tamanho/ 3

if tamanho < 54 == 0:
    latas = tamanho / 54
else:
    latas = int(tamanho / 54) + 1

preco = latas * 80
print('')
print('Você vai precisar de',+latas, 'lata(s).')
print('')
print('O valor é R$','{:.2f}'.format(preco))