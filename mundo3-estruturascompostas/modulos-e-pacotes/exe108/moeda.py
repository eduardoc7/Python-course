def metade(preco=0):
    return preco / 2


def dobro(preco=0):
    return preco * 2


def aumentar(preco=0):
    p = (preco * 10) / 100
    return preco + p


def reduzindo(preco=0):
    p = (preco * 13) / 100
    return preco - p


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

