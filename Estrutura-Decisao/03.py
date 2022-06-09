# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('*•.¸♡ F ou M? ♡¸.•*')

sexo = str(input('F ou M? -> ')).upper() # .upper() converte tudo para maisculo.

if sexo == 'F':
    print(sexo,'- Feminino')
elif sexo == 'M':
    print(sexo,'- Masculino')
else:
    print('opção invalida, tente novamente.')