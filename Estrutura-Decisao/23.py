# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

print('# ----- INTEIRO OU DECIMAL? ----- #')

numero = float(input('Digite o numero: '))

if numero == int(numero):
    print(f'{numero:.0f} é um numero inteiro.')
else:
    print('{} é um numero decimal.'.format(numero))