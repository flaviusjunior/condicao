n = 0
while True:
    n = int(input('\nInforme o numero da Tabuada desejada: '))
    print(f'\nTabuada de "{n}":\n')
    if n < 0:
        break
    for junior in range(1, 11):
        print(f'{n} X {junior} = {n*junior}')
        '''print("%a x %a = %" % (n, junior+1, n*(junior+1)))'''
print('\033[32mTabuada encerrada')
