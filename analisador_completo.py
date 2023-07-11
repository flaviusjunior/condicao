'''Desenvolva um programa que leia o nome
 idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo
 qual é o nome do homem mais velho e quantas mulheres
 têm menos de 20 anos.'''

media_idade = 0
soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ' '
qt_mulheres20 = 0

for p in range(1, 4):
    print('\n------ {} pessoa ------'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma_idade = soma_idade + idade
    if p == 1 and sexo == 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        qt_mulheres20 = qt_mulheres20 + 1

media_idade = soma_idade / 4    
print(f'A media de idadde do grupo é de {media_idade}')
print('O homem mais velho tem {} o seu nome é: {}'.format(maior_idade_homem, nome_mais_velho))
print(f'Temos {qt_mulheres20} mulhres com menos de 20 anos!')

