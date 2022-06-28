'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a:
2 questões-> "Suspeita",
entre 3 e 4 -> "Cúmplice",
5 -> como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

print('# CRIME SCENE #')
print('')
print('Você pode responder apenas sim ou não. Agora me diga...')
print('')

contagem = 0

telefone = str(input('Você telefonou para a vitima?\n').lower())
if telefone == 'sim':
    contagem = + 1

local = str(input('Esteve no local do crime?\n').lower())
if local == 'sim':
    contagem = + 1

moradia = str(input('Você mora perto da vitima?\n').lower())
if moradia == 'sim':
    contagem = + 1

devedor = str(input('Você deve a vitima?\n').lower())
if devedor == 'sim':
    contagem =+1

trabalho = str(input('Você já trabalhou com a vitima?\n').lower())
if trabalho == 'sim':
    contagem =+1

print('....')
print('Obrigada por responder!\n')
print('Esta pessoa é:\n')

if contagem == 0:
    print('INOCENTE.')

if contagem <= 2:
    print('SUSPEITA.')

elif contagem > 5:
    print ('CUMPLICE.')
else:
    print('ASSASSINA.')
print('')
print('Obrigada por utilizar este programa. :)')