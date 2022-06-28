# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('•------» Vogal ou Consoante? «------•')

letra = input('Digite a letra: ').lower()

vogal = ('a','e','i','o','u','y')

consoante = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z')

if letra in vogal:
    print(letra,'-> é vogal.')
elif letra in consoante:
    print(letra,'-> é consoante.')
else:
    print(letra,'-> não é letra.')