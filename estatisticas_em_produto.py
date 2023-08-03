barato = ' '
cont = 0
menor = 0
quant_produto = 0
soma = 0

print('\n=========== Loja Impacto/07 ==========')

while True:

    nome_produto = str(input('\nNome do produto: '))
    preco_produto = float(input('Preço do Produto R$: '))

    cont = cont + 1
    soma = soma + preco_produto

    if preco_produto >= 1000:
        quant_produto = quant_produto + 1

    if cont == 1:
        menor = preco_produto
        barato = nome_produto
    else:
        if preco_produto < menor:
            menor = preco_produto
            barato = nome_produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('\nQuer continuar [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'\nQuantidade de produtos maior que 1000 reais: {quant_produto}')
print(f'Gasto: {soma}')
print(f'Mas Barato: {barato} \ncusta: {menor}\n')
print('-----------FIM DO GPROGRANA--------------')
