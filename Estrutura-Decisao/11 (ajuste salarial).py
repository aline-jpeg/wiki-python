'''
A empresa resolveram dar um aumento de salário e lhe contraram para desenvolver o programa.
Faça um programa que recebe o salário e o reajuste, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:

    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento.

'''

print('# ------ REAJUSTE SALARIAL ------ #')

salario = float(input('Digite o salario: R$ '))

if salario <= 280:
    aumento = salario * (20/100)
    resultado = salario + aumento
    print('Antigo salario: R$',salario, 'Com reajuste de 20% ->',resultado)
elif salario > 280.00 and salario <= 700:
    aumento = salario * (15/100)
    resultado = salario + aumento
    print('Antigo salario: R$',salario, 'Com reajuste de 15% ->',resultado)
elif salario > 700 and salario < 1500:
    aumento = salario * (10/100)
    resultado = salario + aumento
    print('Antigo salario: R$',salario, 'Com reajuste de 10% ->',resultado)
else:
    aumento = salario * (5/100)
    resultado = salario + aumento
    print('Antigo salario: R$',salario, 'Com reajuste de 5% ->',resultado)

print('')
print('# -------------------------- #')