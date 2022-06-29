'''
 O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
                     Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra.
Escreva um programa que peça: 
o tipo e a  quantidade de carne comprada pelo usuário e  gere um cupom fiscal,contendo as informações da compra: 

tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print('----- HIPERMERCADO TABAJARA -----')
print('')
print('Possui cartão da loja?')
print('| 1 | SIM\n| 2 | NÃO')
cartao = int(input(''))

print('Selecione:')
print('| 1 | FILE DUPLO')
print('| 2 | ALCATRA')
print('| 3 | PICANHA')
carne = int(input(''))

print('')
print('Quantos Kgs?')
kg_carne = int(input(''))

# CALCULO PREÇO DA CARNE

if carne == 1:
    nome = "FILE DUPLO"
    if kg_carne <= 5:
        preco = kg_carne * 4.90
    else:
        preco= kg_carne * 5.80

elif carne == 2:
    nome = "ALCATRA"
    if kg_carne <= 5:
        preco = kg_carne * 5.90
    else:
        preco = kg_carne * 6.80

elif carne == 3:
    nome = "PICANHA"
    if kg_carne <= 5:
        preco = kg_carne * 6.90
    else: 
        preco = kg_carne * 7.80

else:
    print('Opção invalida!')

desconto = (preco /100) * 5

# CARTAO DA LOJA

if cartao == 1:
    cartao = "SIM"
    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    cartao = "NÃO"
    total = preco

# MONTAGEM DO NOTA FISCAL
print('')
print('#### CUPOM FISCAL ####')
print(f'CARNE ........... {nome}')
print(f'QUANTIA ......... {kg_carne} kgs')
print(f'PREÇO ........... R$ {preco:.2f}')
print(f'CARTÃO .......... {cartao}')
print(f'DESCONTO ........ R$ {desconto:.2f}')
print(f'TOTAL ........... R$ {total:.2f}')