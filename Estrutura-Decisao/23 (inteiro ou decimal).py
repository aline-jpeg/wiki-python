# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 

print('# ----- INTEIRO OU DECIMAL? ----- #')
print('')

numero = float(input('Digite o numero: '))
print('')
if numero == int(numero):
    print(f'{numero:.0f} é um numero inteiro.')
else:
    print('{} é um numero decimal.'.format(numero))