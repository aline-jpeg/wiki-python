# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# Como calcular a área de um circulo?
# A área de qualquer circulo é igual a :  π  vezes o raio do circulo ao quadrado.
# Fica assim:    A =  π . r²     //sendo π  aproximadamente  3,14.


print('------ AREA DO CIRCULO ------')
print('')


pi = 3.14
raio = float(input ('Digite a area do circulo em mts: '))
area = pi * (raio*raio)
print('A area do circulo é: ', '{:.1f}'.format(area), 'mts²')