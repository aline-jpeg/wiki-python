# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

print('•------» PAR OU IMPAR «------•')

numeros = []
par = []
impar = []

for num in range(0, 20):
    numeros.append(int(input('Digite o numero: ')))

for num in range(0, 20):
    if numeros[num] % 2 == 0: # se o resto da divisao por 2 for 0, entao o numero é par.
        par.append(numeros[num])
    else:
        impar.append(numeros[num])

print('')
print('Numeros digitados:\n',numeros)
print('Par:\n',par)
print('Impar:\n',impar)