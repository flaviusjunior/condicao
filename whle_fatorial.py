from math import factorial
'''Faça um programa que leia um número 
qualquer e mostre o seu fatorial.'''

print('\n========Fatorial=========')

numero = int(input('\nInforme um numero: '))
fatorial = factorial(numero)

print(f'O fatorial de {numero} é: {fatorial}\n')

'''Segunda forma de fazer'''

print('\n========Fatorial=========')

numero = int(input('\nInforme um numero: '))
contador = numero
fatorial = 1

print(f'Calculando fatorial de {numero}! = ',end='')

while contador > 0:

    print(f'{contador}',end='')
    print(' x ' if contador > 1 else ' = ', end='')

    fatorial = fatorial * contador
    contador = contador - 1
    
print(f'{fatorial}')
print(f'O fatorial de {numero} é: {fatorial}\n')
