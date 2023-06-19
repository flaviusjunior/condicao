print('\n===============Conversor de Base numerica===============')

numero = int(input('\nDidite um numero inteiro: '))

print('''\nEsconha a opção da coversçao:
[1] PARA BINARIO
[2] PARA OCTAGONAL
[3] PARA HEXADECIMAL''')
      
opção = int(input('\nOPÇÃO: '))

if opção == 1:
    print('\n{} convertido para Binario é : {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('\n{} convertido para binario é : {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('\n{} convertido para exadecimal é : {}'.format(numero, hex(numero)[2:]))
else:
    print('\nOPÇÃO INVALIDA!!!')