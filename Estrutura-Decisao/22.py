# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

print('----- PAR OU IMPAR? -----')

num = int(input('Digite o numero: '))

if (num%2) == 0: # Se o numero for divido por 2 e sobrar 0, entao é par.
    print('Numero par!')
else:
    print('Numero impar!')