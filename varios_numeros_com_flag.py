numero = 0
contador = 0
soma = 0

while True:
    numero = int(input("\nDigite um numero [999 para PARARS]: "))
    if numero == 999:
        break
    contador = contador + 1
    soma = soma + numero

print(f'\nForam digitados \033[32m{contador} \033[0mnumeros, a soma de todos é \033[32m{soma}\033[0m\n.')
