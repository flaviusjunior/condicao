condicao = 's'
soma = cont = maior = menor = media = 0
while condicao in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma  + num 
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    condicao = str(input('Quer contimuar: ')).upper().strip()[0]

media = soma / cont
print(f'Vc digitou {cont} numeros e a media é : {media:.2f}')
print(f'O maior numero foi o : {maior} e o menor : {menor}')
