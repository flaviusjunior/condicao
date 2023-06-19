print("==="*20)

valor_casa = float(input("Digite o valor da casa desejada: "))
salario = float(input("Digite seu salario: "))
anos = int(input("Quantos anos deseja pagar?:"))

prestação = valor_casa / (anos * 12)
minimo = salario / 100 * 30

print('Pra voce pagar a casa de {:.2f}, em {}'.format(valor_casa, anos))
print('Aprestação sera de {:.2f}'.format(prestação))

if prestação <= minimo:
    print('\033[0;32m Imprestimo Aprovado!!!')
else:
    print('\033[1:31 Emprestimo Negado!!!')
    
print("==="*20)
