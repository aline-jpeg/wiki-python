'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo; 
inteiro ou decimal.
'''

print('# ----- DOIS NUMEROS ----- #')
print('')

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

print('')

opcao = int(input('OPÇÕES: \n\n1 - SOMA || 2 - SUBTRAÇÃO || 3 - MULTIPLICAÇÃO || 4 - DIVISÃO \n\nDigite a opção desejada -> '))

print('')

if opcao == 1:
    soma = num1 + num2
    print(f'O resultado é:\n{soma:.0f}')
    if soma%2 == 0:
        print('par.')
    else:
        print('impar.')
    if soma > 0:
        print('positivo.')
    else:
        print('negativo.')
    if soma == int:
        print('inteiro.')
    else:
        print('decimal.')


elif opcao == 2:
    sub = num1 - num2
    print(f'O resultado é:\n{sub:.0f}')
    if sub%2 == 0:
        print('par')
    else:
        print('impar')
    if sub > 0:
        print('positivo')
    else:
        print('negativo')
    if sub == int:
        print('inteiro.')
    else:
        print('decimal.')


elif opcao == 3:
    mult = num1 * num2
    print(f'O resultado é:\n{mult:.0f}')
    if mult%2 == 0:
        print('par')
    else:
        print('impar')
    if mult > 0:
        print('positivo')
    else:
        print('negativo')    
    if mult == int:
        print('inteiro.')
    else:
        print('decimal.')


elif opcao == 4:
    div = num1 / num2
    print(f'O resultado é:\n{div:.0f}')
    if div%2 == 0:
        print('par')
    else:
        print('impar')
    if div > 0:
        print('positivo')
    else:
        print('negativo')
    if div == int:
        print('inteiro.')
    else:
        print('decimal.')


else:
    print('OPÇÃO INVALIDA')