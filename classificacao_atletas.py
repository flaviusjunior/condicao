
'''A Confederação Nacional de Natação precisa de 
um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:'''


print('\n============= Classificação de Atleta================\n')

from datetime import date
atual = date.today().year
data_nascimento = int(input('Digite o ano de nacimento do Atleta: '))
idade = atual - data_nascimento

if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim.\n')
elif idade > 9 and idade <=14:
    print('CLASSIFICAÇÃO: Infantil.\n')
elif idade > 14 and idade <= 19:
    print('CLASSIFICAÇÃO: Junior.\n')
elif idade > 19 and idade <= 25:
    print('CLASSIFICAÇÃO: Senior.\n')
else:
    print('Master.')
