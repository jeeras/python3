num = 0
soma = 0
cont = 0
while not num == 999:
    num = int(input('Digite um número [999 para parar o programa]: '))
    soma = soma + num
    cont = cont + 1
    if num == 999:
        cont = cont - 1
        soma = soma - 999
print('A soma de todos os números é {}'.format(soma))
print('Há ao todo {} numero(s)'.format(cont))