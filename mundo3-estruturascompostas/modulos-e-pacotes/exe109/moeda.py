def metade(preco=0, formatar=False):
    res = preco / 2
    return res if formatar is False else moeda(res)


def dobro(preco=0, formatar=False):
    res = preco * 2
    return res if formatar is False else moeda(res)


def aumentar(preco=0, formatar=True):
    res = preco + (preco * 10) / 100
    return res if formatar is False else moeda(res)


def reduzindo(preco=0, formatar=True):
    res = preco + (preco * 13) / 100
    return res if formatar is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


