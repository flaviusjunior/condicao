print('\n========= LOJA ===========')

preço = float(input('Qual o preço do produto: '))
print('FORMA DE PAGAMENTO:\n(1) DINHEIRO\n(2) Á vita no Cartão\n(3) 2 X no Cartão\n(4) 3 x ou mais no Cartão')
opção = int(input('\nQual a forma de pagamento: '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Valor do produto será de {}'.format(((preço / 100) * 90)))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Valor do produto {} será de {}'.format(preço, total))
elif opção == 3:
    total = preço
    parcelas = total / 2
    print('Valor do produto {} será de 2 parcelas de {} '.format(preço, parcelas))
elif opção == 4:
    quant_parcelas = int(input('Quantas Parcelas: '))
    total = preço + (preço * 20 / 100)
    parcelas = total / quant_parcelas
    print('Valor do produto de {}, terá {} parcelas com juros de {}, com o Total de {}'.format(preço, quant_parcelas, parcelas, total))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE !!!')
