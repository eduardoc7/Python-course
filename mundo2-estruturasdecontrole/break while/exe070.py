nomeProduto = nomemaisbarato = ''
price = soma = maisdemil = maisbarato = 0
c = 1
while True:
    nomeProduto = str(input('Type the product name: '))
    price = float(input('Price: U$'))
    soma += price
    opcao = ' '
    if price > 1000:
        maisdemil += 1
    if c == 1:
        nomemaisbarato = nomeProduto
        maisbarato = price
    if price < maisbarato:
        maisbarato = price
    while opcao not in 'YN':
        opcao = str(input('Do you want to continue? [Y/N] ')).upper().strip()
    if opcao in 'N':
        break
    c += 1
print('FIM DO PROGRAMA')
print(f'Total da compra foi {soma}')
print(f'Temos {maisdemil} custando mais de U$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa {maisbarato}')
