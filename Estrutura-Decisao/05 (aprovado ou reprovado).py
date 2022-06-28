# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('•------» Aprovado ou Reprovado? «------•')

nota = float(input('Digite a nota do aluno: '))

if nota == 10.0:
    print('10? Aprovado com Distinção!')
elif nota >= 7.0:
    print('Aprovado! Nota ->',nota)
else:
    print('Reprovado! Nota ->',nota)