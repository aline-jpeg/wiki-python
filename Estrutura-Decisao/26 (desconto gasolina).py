'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro. 
acima de 20 litros, desconto de 5% por litro.

Gasolina:
até 20 litros, desconto de 4% por litro. 
acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível:
        A - álcool 
        G - gasolina 

Calcule e imprima o valor a ser pago pelo cliente sabendo-se que:
    O litro da gasolina é R$ 2,50 
    O litro do álcool é R$ 1,90.

'''
print('----- POSTO DA ESTRADA -----')
print('')
print('Por favor, digite: ')
print('1 - para Alcool')
print('2 - para Gasolina:')
opcao = int (input('   '))

alcool = 1.90
gasolina = 2.50


if opcao == 1:
    print('Quantos litros de alcool?')
    litrosalcool = int(input(''))
    if litrosalcool <= 20:
        quantiaalcool = alcool * litrosalcool
        desconto = (quantiaalcool / 100) * 3
        total = quantiaalcool - desconto
    elif litrosalcool > 20:
        quantiaalcool = alcool * litrosalcool
        desconto = (quantiaalcool / 100) * 5
        total = quantiaalcool - desconto
    print('')
    print(f'Para {litrosalcool} litros de alcool, terá desconto de R$ {desconto:.2f}.') 
    print(f'Total a pagar com desconto: R$ {total:.2f}')

elif opcao == 2:
    print('Quantos litros de gasolina?')
    litrosgasolina = int(input(''))
    if litrosgasolina <= 20:
        quantiagasolina = gasolina * litrosgasolina
        desconto = (quantiagasolina / 100) * 4
        total = quantiagasolina - desconto
    elif litrosgasolina > 20:
        quantiagasolina = gasolina * litrosgasolina
        desconto = (quantiagasolina / 100) * 6
        total = quantiagasolina - desconto
    print('')
    print(f'Para {litrosgasolina} litros, terá desconto de R$ {desconto:.2f}. ')
    print(f'Total a pagar com desconto: R$ {total:.2f}')
    

else:
    print('Opção invalida, tente novamente.')