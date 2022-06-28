# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


print('------ PESO IDEAL 2 ------')
print('')


altura = float(input('Digite altura: '))
sexo = int(input('Digite:\n1 para homem || 2 para mulher -> '))

if sexo == 1:
    peso1 = (72.7 * altura) -58
    print('PESO IDEAL (HOMEM) ->','{:.2f} KGS'.format(peso1))
else:
    peso2 = (62.1 * altura) - 47
    print('PESO IDEAL (MULHER )->','{:.2f} KGS'.format(peso2))