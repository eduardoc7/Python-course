def escreva(texto):
    print('~' * len(texto))
    print(f'{texto}')
    print('~' * len(texto))


# Main Program
msg = str(input('Digite uma mensagem qualquer para testar nossa função: '))
escreva(msg)
