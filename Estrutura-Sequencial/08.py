# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Valor hora: '))
horasTotal = float(input('Horas trabalhadas: '))

salario = valorHora * horasTotal

print('Valor a receber: R$ ', +salario)