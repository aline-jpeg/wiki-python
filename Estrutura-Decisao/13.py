# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('# ----- DIA DA SEMANA ----- #')

numDia = int(input('Digite o numero do dia da semana: '))

if numDia == 1:
    print('01 - Domingo')
elif numDia == 2:
    print('02 - Segunda-Feira')
elif numDia == 3:
    print('03 - Terça-Feira')
elif numDia == 4:
    print('04 - Quarta-Feira')
elif numDia == 5:
    print('05 - Quinta-Feira')
elif numDia == 6:
    print('06 - Sexta-Feira')
elif numDia == 7:
    print('07 - Sabado')
else:
    print('Valor invalido! Tente novamente.')