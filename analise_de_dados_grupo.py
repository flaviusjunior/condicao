contador_idade = 0
cont_masculino = 0
cont_feminino = 0
resposta = ' '
cont_20 = 0
cont_18 = 0
while True:
    print('\n=============================')
    print('Cadastre uma Pessoa')
    print('=============================')

    idade = int(input('\nQual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [ M / F ]: ')).strip().upper()[0]
    if idade >= 18:
        cont_18 = cont_18 + 1
    if idade >= 20 and sexo == 'F':
        cont_20 = cont_20 + 1
    if sexo == 'M':
        cont_masculino = cont_masculino + 1
    else:
        cont_feminino = cont_feminino + 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('\nVc quer continuar: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'\nPessoas com mas de 18 anos: {cont_18}')
print(f'Homens: {cont_masculino}, Mulheres {cont_feminino}')
print(f'Mulheres com mais de 20 anos: {cont_20}\n')
