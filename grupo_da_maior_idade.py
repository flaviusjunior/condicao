from datetime import date
data_atual = date.today().year

total_maior = 0
total_menor = 0

for pessoas in range(0, 7):    
     ano = int(input('qual o ano de nascimento: '))
     idade = data_atual - ano
     if idade >= 21:
        total_maior = total_maior + 1
     else:
        total_menor = total_menor + 1

print('\033[32mTivemos {} pessoas maiores de idade'.format(total_maior))
print('\33[34mTambém tivemos {} pessoas menores de idade'.format(total_menor))
