from time import sleep
maior18 = 1
homens = 0
menos20 = 1
print('--- Cadastre uma pessoa ---')
while True:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo  = str(input('Informe o sexo da pessoa [M/F]: ')).upper().strip()[0]
    op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if op == 'N':
        break
    elif op == 'S':
        print('Ok...')
        sleep(1)
        print('=' * 20)
    else:
        print('Opção inválida')
    if idade > 18:
        maior18 = maior18 + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        menor20 = menor20 + 1
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Total de homens que foram cadastrados: {homens}')
print(f'Total de meninas com menos de 20 anos: {menor20}')
