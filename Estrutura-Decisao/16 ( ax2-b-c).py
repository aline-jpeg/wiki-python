'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado.

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

'''

print(' ---- ax2 + bx + c  ---- ')
print('')

a = int(input('Digite o valor de a: '))
if a == 0:
    print('ERRO. A equação não é de segundo grau.')
else:
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = ((b,2) - (4* a * c))
    if delta < 0:
        print("delta = ",delta," a equacao nao possui raizes reais")     
    if delta == 0:
        print ("delta = ",delta," a equacao possui uma raiz")
    raiz = ((-1)*b + (delta))/(2*a)
    print ("raiz da equacao = ", raiz)
    if delta > 0:
        raiz1 = ((-1)*b + (delta)) / (2*a)
        raiz2 = ((-1)*b - (delta)) / (2*a)
        print ("raiz1 da equacao = ", raiz1)
        print ("raiz2 da equacao = ", raiz2)
print('')
print('-----------------------')