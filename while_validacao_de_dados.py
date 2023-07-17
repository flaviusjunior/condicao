'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''
s = str(input('\nDigite o sexo da pessoa [M ou F]: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('\nResposta invalida! Digite novamente: '))
print('sexo registrado com sucesso!!!')