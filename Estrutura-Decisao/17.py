# Faça um Programa que peça um número correspondente a um determinado ano 
# e em seguida informe se este ano é ou não bissexto.

# Levando em consideração que todo ano bissexto é multiplo de 4:
# Mas tem exceção: múltiplos de 100 que não sejam múltiplos de 400.

ano = int(input('Digite o ano: '))

if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
    print('ano bissexto!')
else:
    print('não é bissexto.')