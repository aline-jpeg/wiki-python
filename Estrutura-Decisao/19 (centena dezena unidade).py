'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. 

Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
print('----- NUMEROS -----')
print('')

numero = int(input('Digite um numero até 1000: '))

if numero <= 1000:
    centena = int(numero / 100)
    dezena = int((numero % 100) / 10)
    unidade = numero % 10
    print(f'{numero} = {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')
else:
    print('Numero invalido! Digite um numero até 1000.')