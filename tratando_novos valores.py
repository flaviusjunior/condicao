"""Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag)."""
num = 0
soma = 0
cont = 0
while num != 999:
    soma = soma + num
    cont = cont + 1    
    num = int(input('Digite um numero [999 para Parar] : '))

print(f'Parabéns {cont - 1} numeros a soma de todos é : {soma}')




