# v3.0

valor = 0
cont = 0
while True:
    valor = int(input('Digite um número para ver sua tabuada [Um valor negativo finaliza o programa]:  '))
    if valor < 0:
        break
    for c in range(1, 11):
        cont = cont + 1
        print('{} x {} = {}'.format(valor, cont, valor * cont))
print('Programa finalizado.')