'''
Faça um programa que lê as duas notas parciais obtidas por um aluno em um semestre.
Calcule a sua média, a atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0            A
    Entre 7.5 e 9.0             B
    Entre 6.0 e 7.5             C
    Entre 4.0 e 6.0             D
    Entre 4.0 e zero            E

'''
print('------- NOTAS FINAIS -------')
print('')
av1 = float(input('Digite nota da av1: '))
av2 = float(input('Digite nota da av2: '))

nota = (av1 + av2) / 2
print('')
if nota > 9.0:
  print(f'Media do aluno: {nota:.2f}')
  print('|| Conceito: A ||')
elif nota < 9.0 and nota > 7.5:
  print(f'Media do aluno: {nota:.2f}')
  print('|| Conceito: B ||')
elif nota < 7.5 and nota > 6.0:
  print(f'Media do aluno: {nota:.2f}')
  print('|| Conceito: C ||')
elif nota < 6.0 and nota > 4.0:
  print(f'Media do aluno: {nota:.2f}')
  print('|| Conceito: D ||')
elif nota < 4.0 and nota > 0:
  print(f'Media do aluno: {nota:.2f}')
  print('|| Conceito: E ||')
else:
  print('')
  print('Notas invalidas, tente novamente.')
print('')
print('-------------------')