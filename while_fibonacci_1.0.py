print('\n========Sequencia de Fibonacci==========')
numeros_termos = int(input("\nDigite o Numero de termos q vc quer mostrar : "))

penultima = 1
ultima = 1

print('/'*40)

print(f'{penultima} -> {ultima}', end='')

cont = 3

while cont <= numeros_termos:
    
    atual = penultima + ultima
    print(f' -> {atual}', end='')

    penultima = ultima
    ultima = atual
    cont = cont + 1


print(" -> fim")
print('/'*40)


n = int(input("\033[32m\nDigite o Numero de\033[m termos q vc quer mostrar : "))

penultima = 0
proximo = 1
#print(penultima, end='')
print(f'{penultima} -> {proximo}', end='')

for j in range(2, n):
    atual = proximo + penultima
    penultima = proximo
    proximo = atual
    print(f' -> {atual}', end='')
