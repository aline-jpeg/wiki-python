'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00: 
Receberá ainda um desconto de 10% sobre este total. 

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

'''

print('------ FRUTARIA ------ ')
print('')
print('Quantos kgs de morangos?')

kg_morango = int(input(''))

print('Quantos kgs de maçãs?')

kg_maca = int(input(''))

# MORANGOS:
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

# MAÇÃS:
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total = preco_morango + preco_maca

# DESCONTO ADICIONAL:
quantia_total = kg_morango + kg_maca

if quantia_total > 8 or total > 25.00:
    desconto = (total / 100) * 10
    total = total - desconto

print('')
print(f'Total: R$ {total:.2f}')
print('')
print('Obrigada por comprar conosco, volte sempre! :)')