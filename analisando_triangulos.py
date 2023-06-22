'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''

print('***'*20)

r1 = float(input("\nDigite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\nAs retas acima PODE formar um triangulo!")
    if r1 == r2 and r3:
        print('Esse é um Triangulo EQUILÁTERO !!! ')
    elif r1 != r2 != r3 != r1:
        print('Esse é um Triangulo ESCALENO !!! ')
    else:
        print('Esse é um Triangulo ISÓCELES !!! ')
else:
    print('Não pode formar um triangolo !!! ')
