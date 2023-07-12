'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai 
tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10)

print("Sou seu computador pensei em um numero tente adivinhar!")

acertou = False
palpites = 0

print('\n==========JODO DA ADIVINHAÇÃO=========== ')

while not acertou:
    jogador = int(input('\nAdivinhe o numero entre [0 e 10]:'))
    palpites = palpites +1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('[+] Tenta de novo!')
        elif jogador > computador:
            print('[-] tenta de novo!')
print(f'\033[32mPARABÉNS!!! Vc tentou {palpites} vezes\n')



tentativas = 0
num = 0
print('\n==========JODO DA ADIVINHAÇÃO=========== ')
while num != 9:
    num = int(input('\nAdivinhe o numero entre [0 e 10]:'))
    tentativas = tentativas +1
print(f'\033[32mPARABÉNS!!! Vc tentou {tentativas} vezes\n')

