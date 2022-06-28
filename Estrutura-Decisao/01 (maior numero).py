# Faça um Programa que peça dois números e imprima o maior deles.

print('------- Qual o maior? -------')
print('')

num1 = int(input ('Digite o numero -> '))
num2 = int(input ('Outro numero -> '))

if num1 > num2:
    print(num1,'é maior que',+num2,'.')
else:
    print(num2, 'é maior que',+num1,'.')

print('')
print('-------')