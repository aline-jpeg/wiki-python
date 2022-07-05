# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

print('•------» NUMEROS INTEIROS «------•')

numeros = []
print ('Informe os 5 numeros:')
for i in range(5):
 	numeros.append(input(''+ str(i+1) + ': '))
print (numeros) 