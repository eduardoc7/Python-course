def area(largura, comprimento):
    print(f'A área deste terrno é de {largura}x{comprimento} é de {largura*comprimento}')


# Main Program
print('     CONTROLE DE TERRENOS')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
