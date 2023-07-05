n = int(input('digite o numero: '))
total = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(c), end=' ')

print(f'\n\033O numero {c}, foi divizivel {total} vézes')

if total == 2:
    print('Portanto ele é PRIMO!')
else:
    print('NÃO é PRIMO!')
