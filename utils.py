codigos_cores = ['[37m', '[33m', '[31m']
nomes_cores = ['branco', 'amarelo', 'vermelho']


def texto_com_cor(texto, cor = 'branco'):
    index = nomes_cores.index(cor)
    return f'\033{codigos_cores[index]} {texto} \033{codigos_cores[0]}'

def color_print(mensagem, cor = 'branco'):
    texto = texto_com_cor(mensagem, cor)
    print(texto)

def int_input(mensagem, cor = 'azul'):
    texto = texto_com_cor(mensagem, cor)
    return int(input(texto))

def flot_input(mensagem, cor = 'azul'):
    texto = texto_com_cor(mensagem, cor)
    return float(input(texto))