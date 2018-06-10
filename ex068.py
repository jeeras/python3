from random import randint
from time import sleep
contwin = 0
contlose = 0
print('-' * 20)
print('JOGO DO PAR OU ÍMPAR')
print('-' * 20)
while True:
    jogadavalor = int(input('Digite um valor: '))
    jogadapi = str(input('PAR OU ÍMPAR? [P/I]')).upper().strip()[0]
    jogadapc = randint(1, 10)
    if jogadapi == 'P' and (jogadavalor + jogadapc) % 2 == 0:
        contwin = contwin + 1
        print(f'Você jogou {jogadavalor} e o computador jogou {jogadapc}, ou seja deu PAR.')
        print('Você ganhou!')
        print('Vamos jogar novamente?')
        sleep(2)
    elif jogadapi == 'P' and (jogadapc + jogadavalor) % 2 != 0:
        contlose = contlose + 1
        print(f'Você jogou {jogadavalor} e o computador jogou {jogadapc}, ou seja deu ÍMPAR.')
        print('Você perdeu...')
        break
    elif jogadapi == 'I' and (jogadavalor + jogadapc) % 2 != 0:
        contwin = contwin + 1
        print(f'Você jogou {jogadavalor} e o computador jogou {jogadapc}, ou seja deu ÍMPAR.')
        print('Você ganhou!')
        print('Vamos jogar novamente?')
        sleep(2)
    elif jogadapi == 'I' and (jogadapc + jogadavalor) % 2 == 0:
        contlose = contlose + 1
        print(f'Você jogou {jogadavalor} e o computador jogou {jogadapc}, ou seja deu PAR.')
        print('Você perdeu...')
        break
    else:
        print('Jogada inválida.')
print(f'Você ganhou {contwin} vezes')