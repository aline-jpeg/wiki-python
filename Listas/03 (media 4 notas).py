# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


print('•------» MEDIA DO ALUNO «------•')
notas = []

print('Digite as notas do aluno:')

for i in range(4):
    notas.append(float(input(''+ str(i+1) + ': ')))
    media = (1 + 2 + 3 + 4) / 2

print(f'A media do aluno é: {media:.1f}')