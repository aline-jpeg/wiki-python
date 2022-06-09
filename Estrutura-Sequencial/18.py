'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''

print('		░▒▓█ TEMPO DOWNLOAD █▓▒░')

arquivo = int(input('Tamanho do arquivo em MB: '))

link = int(input('Velocidade em mbps --> '))

tempo = (arquivo / (link / 8)) / 60 # ----- 8 bits equivalem a 1 byte.

print(f'Arquivo: {arquivo}MB || velocidade {link}mbps\nTempo estimado de download: {tempo:.0f}\n')