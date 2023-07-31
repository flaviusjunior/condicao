from random import randint
vitoria = 0
print('\n==================Jogo Par ou Impar==================\n')
while True:
    jogador = int(input('\nDiga o seu valor: '))
    computador = randint (0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Voçê jogou: {jogador} e o computador: {computador}\nresultado: {total}!')
    print('\033[32mDeu PAR' if total % 2 == 0 else 'Deu IMPAR\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc VENCEU')
            vitoria = vitoria + 1
        else:
            print('\033[31mVc PERDEU\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vc VENCEU')
            vitoria = vitoria + 1
        else:
            print('\033[31mVc PERDEU\033[m')
            break

print(f'vc ganhou: {vitoria} vezes')
