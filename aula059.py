from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print("""
    [ 1 ] Somar os valores
    [ 2 ] Multiplicar os valores
    [ 3 ] Qual é o maior valor
    [ 4 ] Novos valores
    [ 5 ] Sair do programa
    """)
    opcao = int(input('Qual sua opção: '))
    if opcao == 1:
        print('A soma desses dois valores é: {}'.format(n1 + n2))
        sleep(3)
    elif opcao == 2:
        print('Esses dois valores multiplicados são {}'.format(n1 * n2))
        sleep(3)
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior comparado ao {}'.format(n1, n2))
            sleep(3)
        else:
            print('{} é o maior comparado ao {}'.format(n2, n1))
            sleep(3)
    elif opcao == 4:
        n1 = float(input('Primeiro novo valor: '))
        n2 = float(input('Segundo novo valor'))
        sleep(1.5)
    else:
        print('Muito obrigado, e tenha um bom dia')
print('fim do programa')