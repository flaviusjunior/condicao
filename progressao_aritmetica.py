print('==='*13)
print('        10 TERMOS DE UMA PA')
print('==='*13)

p = int(input('Digite o primeiro termo: '))
r = int(input('RAZÃO: '))
decimo = p + (10 - 1) * r

for i in range(p, decimo + r, r):
    print(i, end=' -> ')
    
print('ACABOU')
