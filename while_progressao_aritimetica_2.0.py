print('==='*13)
print('        10 TERMOS DE UMA PA')
print('==='*13)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('RAZÃO: '))
termo = primeiro
cont = 1
total = 0
mostrar = 10
while mostrar != 0:
    total = total + mostrar
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont = cont + 1
    print('ACABOU')
    mostrar = int(input('\nQuantos termos quer mostrar a mais? '))
print('fim')
