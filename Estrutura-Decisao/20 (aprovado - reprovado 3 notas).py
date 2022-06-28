'''
Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
print('----- APROVADO OU REPROVADO -----')

av1 = float(input('Digite a nota av1: '))
av2 = float(input('Digite a nota av2: '))
av3 = float(input('Digite a nota av3: '))

media = (av1 + av2 + av3) / 2

if media >= 10:
    print('Aprovado com Distinção!')
elif media > 7:
    print('Aprovado!')
elif media < 7:
    print('Reprovado')
else:
    print('Erro. Tente novamente.')