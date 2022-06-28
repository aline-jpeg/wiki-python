'''
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    Triângulo Equilátero ---> três lados iguais
    Triângulo Isósceles  ---> quaisquer dois lados iguais
    Triângulo Escaleno   ---> três lados diferentes
'''

print('--- TRIANGULOS ---')
print('')

lado1 = float(input('Digite lado 1: '))
lado2 = float(input('Digite lado 2: '))
lado3 = float(input('Digite lado 3: '))

print('')

if lado1 == lado2 and lado2 == lado3:
    print('Triangulo do tipo Equilatero.')
elif lado1 == lado2 or lado2 == lado3:
    print('Triangulo do tipo Isosceles.')
else:
    print('Triangulo do tipo Escaleno.')

print(' /\ /\ /\ /\ /\ /\  ')