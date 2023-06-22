"""Desenvolva uma lógica que leia o peso
 e a altura de uma pessoa, calcule seu Índice 
 de Massa Corporal (IMC) e mostre seu status,
 de acordo com a tabela abaixo:"""

peso = float(input('\nQual seu peso: '))
altura = float(input('Qual sua altura: '))

imc = peso / (altura ** 2)

print("Seu IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print('Abaixo do Peso !!!')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal !!!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso !!!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE !!!')
else:
    print('OBESIDADE MÓRBIDA !!!')
