# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('----- DATA VALIDA -----')
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

data_valida = False

# meses com 31 dias:
if (mes == 1 or mes ==3 or mes ==5 or mes == 7 or mes == 8 or mes ==10 or mes == 12):
    if dia > 0 and dia <= 31:
        data_valida = True

# meses com 30 dias:
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if dia > 0 and dia <=30:
        data_valida = True

# ano bissexto:
elif mes == 2:
    if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
        if dia > 0 and dia <= 29:
            data_valida = True
        elif dia > 0 and dia <= 28:
            data_valida = True

if data_valida:
    print('A data: ',dia,'/',mes,'/',ano, 'é valida!')
else:
    print('Data invalida, tente novamente.')