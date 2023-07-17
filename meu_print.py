codigos_cores = ['[34m', '[33m', '[31m']
nomes_cores = ['azul', 'amarelo', 'vermelho']

def meu_print(mensagem, cor = 'azul'):
    index = nomes_cores.index(cor)

    print(f'\033{codigos_cores[index]} {mensagem} \033{codigos_cores[0]}\n')