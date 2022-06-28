'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados: 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. 

Faça um programa que nos dê:

☀ salário bruto.
☀ quanto pagou ao INSS.
☀ quanto pagou ao sindicato.
☀ o salário líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

'''

print('------ DESCONTO PAGAMENTO ------')
print('')


valorHora = float(input('Valor da hora trabalhada -> R$ '))
horasTrabalhadas = float(input('Horas trabalhadas -> '))

salarioBruto = (valorHora * horasTrabalhadas) * 30

descontoIr = (salarioBruto / 100) * 11
descontoInss = (salarioBruto /100) * 8
descontoSind = (salarioBruto/100) * 5


salarioLiquido = salarioBruto - (descontoIr + descontoInss + descontoSind)

print('')
print('SALARIO BRUTO-> R$','{:.2f}'.format(salarioBruto))
print('')
print('Você pagou:')
print('')
print('R$','{:.2f}'.format(descontoIr), 'ao Imposto de Renda')
print('')
print('R$','{:.2f}'.format(descontoInss), 'ao INSS')
print('')
print('R$','{:.2f}'.format(descontoSind), 'ao Sindicato')
print('')
print('SALARIO LIQUIDO -> R$','{:.2f}'.format(salarioLiquido))