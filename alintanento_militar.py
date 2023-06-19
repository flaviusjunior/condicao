from datetime import date

print('========== Alistamento Militar =============')

ano = int(input('\nQual ano que vocé nasceu?: '))

data_atual = date.today().year
alistamento = (data_atual - ano)
idade = data_atual -ano 

if alistamento < 18:
    falta = 18 - idade
    print('Ainda não chego o tempo')
    print('Falta {}'.format(falta))
elif alistamento == 18:
    print('Chegou a Hora!')
elif alistamento > 18:
    passou = idade - 18
    print('Passou da hora de se alistar!')
    print('Passou {} anos'.format(passou))
