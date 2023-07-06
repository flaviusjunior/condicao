soma = 0
contador = 0
for crud in range(1, 501, 2):
    if crud % 3 == 0:
        contador = contador + 1
        soma = soma + crud
print('A soma dos numeros multiplos de 3 é: {}, com {} numeros somados!'.format(soma, contador))
print('fim')
