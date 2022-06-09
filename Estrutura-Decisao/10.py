# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('•------» Estuda em qual horario? «------•')

print('Estuda em qual periodo?\n',
'Para periodo Matutino -> M\n',
'Para periodo Vespertino -> V\n',
'Para periodo Noturno -> N')

horario = str(input()).lower()

if horario == ('m'):
    print('Bom dia!')
elif horario == ('v'):
    print('Boa tarde!')
elif horario == ('n'):
    print('Boa noite!')
else:
    print('Valor inválido!')