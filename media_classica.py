'''Calculando a media do aluno!'''

print('\n========== MEDIA ===========')

nota1 = float(input('\nDigite a primeira Nota: '))
nota2 = float(input('Digite a segunda Nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Aprovado!!! sua media foi {media}\n')
elif media >= 5 and media < 7:
    print(f'Recuperação!!! sua media foi {media}\n')
elif media < 5:
    print(f'Reprovado!!! sua media foi {media}\n')
else:
    print('Tente novamente!!!\n')
