# Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('•------» ORDEM DECRESCENTE «------•')

lista = [] # Lista vazia para receber input

for numero in range(3):
    numero = int(input('Digite o numero:'))
    lista.append(numero) 
lista.sort(reverse = True)

print('Ordem decrescente -> ' ,lista)