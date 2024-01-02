#exercicios
#tuplas são imutaveis
lanche = ('anburgue', 'suco', 'pizza', 'pudim')
print (lanche [1:])

for c in lanche:
    print (f'Eu quero {c}')

for cont in range(0, len(lanche)):
    print (f'Eu quero {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu quero {pos}-{comida}')
