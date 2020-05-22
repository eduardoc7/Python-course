def resumo(preco=0, aumento=0, reducao=0):
    a = preco + (preco * aumento) / 100
    r = preco - (preco * reducao) / 100
    print('-' * 40)
    print(f'{"REUSMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço Analisado: {preco:>10}')
    print(f'Dobro do preço: {preco*2:>10}')
    print(f'Metade do preço: {preco/2:>10}')
    print(f'{aumento}% de aumento: {a:>10}')
    print(f'{aumento}% de redução: {r:>10}')
    print('-' * 40)