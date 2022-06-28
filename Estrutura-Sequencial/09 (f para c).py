# Faça um Programa que peça a temperatura em graus Fahrenheit.
# Transforme e mostre a temperatura em graus Celsius. 
# C = 5 * ((F-32) / 9).


print('------ F TO C ------')
print('')


tempF = float(input('Temperatura Fahrenheit: '))

tempC = 5 * ((tempF - 32)/9 )

print('Temperatura Celsius: {:.1f}'.format(tempC))