frase = str(input('Digite a frase: ')).strip() .upper()
palavra = frase.strip()
junto = ''.join(palavra)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso = junto[letra]'''
if inverso == junto:
    print('\033[32m temos um palindromo!')
else:
    print('\033[31m Nao temos um polindromo!')