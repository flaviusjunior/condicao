print('==='*20)
print('\033[32mBANCO DA OPORTUNIDADE\033[m'.center(60))
print('==='*20)

saqui = int(input('Valor do Saque: '))
total = saqui
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total = total - cedula
        total_cedula = total_cedula + 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cedulas de R$: {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('\nAgradecemos a confiaça!!!')
