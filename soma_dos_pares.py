soma = 0
cont = 0

for junior in range(1, 7):
    n = int(input(f'informe o {junior} numero: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
        
print(f'voce informpu {cont} numeros pares e a soma é {soma}.')
