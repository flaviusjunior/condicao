from time import sleep
print('\n                  ========MENU OPÇÕES==========\n')

opcao = 4
somar = 0
multiplicar = 0
while opcao != 5:

    valor1 = int(input('\nDigite o primeiro numero: '))
    valor2 = int(input('digite o segundo numero: '))
    print('\n [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos numeros\n [5] Sair do programa')

    opcao = int(input('\nOPÇÃO: '))

    if opcao == 1:

        somar = valor1 + valor2
        print(somar)
 
    elif opcao == 2:

        multiplicar = valor1 * valor2
        print(multiplicar)

    elif opcao == 3:

        if valor1 > valor2:
            print(valor1)
        else:
            print(valor2)

    elif opcao == 5:
        print('\nFinalizando....')
    
    else:
        print('Invalido... Tente novamente.')

''' elif opcao == 4:
        valor1 = int(input('\nDigite o primeiro numero: '))
        valor2 = int(input('digite o segundo numero: '))
        print('\n [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos numeros\n [5] Sair do programa')
        opcao = int(input('\nOPÇÃO: '))'''

sleep(2)
print('\nFIM...')


