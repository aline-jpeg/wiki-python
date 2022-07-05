# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

print('•------» ORDEM INVERSA «------•')

numeros_reais = []
print ('Informe os 10 numeros reais:')
for i in range(10):
	numeros_reais.append(int(input(''+ str(i+1) + ': ')))
numeros_reais.reverse()
print ('A ordem inversa a sua digitação é: ',numeros_reais)