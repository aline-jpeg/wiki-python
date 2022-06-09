# Faça um Programa que peça a temperatura em graus Celsius. 
# Transforme e mostre em graus Fahrenheit.

tempC = float(input('Temperatura Celsius: '))
tempF = ((tempC * 9/5) + 32)

print('Temperatura Fahrenheit: {:.1f}'.format(tempF))