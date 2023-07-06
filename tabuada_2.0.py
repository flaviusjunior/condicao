n = int(input('Informe o numero desejado: '))
print(f'Tabuada de "{n}":\n')

for junior in range(1, 11):
    print(f'{n} X {junior} = {n*junior}')
    '''print("%a x %a = %" % (n, junior+1, n*(junior+1)))'''
