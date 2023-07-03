from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('=-='*15)
print('''Suas opcões:
[1] Pedra
[2] Papel
[3] Tesoura ''')
jogador = int(input('Digite sua opção:'))
print('Pedra')
sleep(2)
print('Papel')
sleep(2)
print('Tesoura')
print('=-='*15)
print('O computator jogou [{}]'.format(itens[computador]))
print('O Jogador jogou [{}]'.format(itens[jogador]))
print('=-='*15)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('Jogada Invalida!')

if computador == 1: # computador jogou papel
    if jogador == 0:        
        print('Computador Venceu!')
    elif jogador == 1:        
        print('Empate!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogada Invalida!')

if computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('Jogador Venceu!!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Invalida!')


