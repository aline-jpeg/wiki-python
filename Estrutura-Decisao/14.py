'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre.
Calcule a sua média, a atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0            A
  Entre 7.5 e 9.0             B
  Entre 6.0 e 7.5             C
  Entre 4.0 e 6.0             D
  Entre 4.0 e zero            E

'''
print('------- NOTAS FINAIS -------')
av1 = float(input('Digite nota da av1: '))
av2 = float(input('Digite nota da av2: '))

nota = (av1 + av2) / 2

if nota > 9.0:
  print(f'Media do aluno: {nota:.2f} || Conceito: A')
elif nota < 9.0 and nota > 7.5:
  print(f'Media do aluno: {nota:.2f} || Conceito: B')
elif nota < 7.5 and nota > 6.0:
  print(f'Media do aluno: {nota:.2f} || Conceito: C')
elif nota < 6.0 and nota > 4.0:
  print(f'Media do aluno: {nota:.2f} || Conceito: D')
elif nota < 4.0 and nota > 0:
  print(f'Media do aluno: {nota:.2f} || Conceito: E')
else:
  print('Invalido, tente novamente.')
print('-------------------')