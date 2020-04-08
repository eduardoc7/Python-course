preço = float(input('Digite o preço do produto: R$'))
desconto = preço - (preço*5/100)

print('Um produto que custava {:.2f}, com um desconto de 5% passou a custar {:.2f}'.format(preço,desconto))