def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO!')
        if ok:
            break
    return valor


# Main Program
n = leiaint('Digite um número: ')
print(f'Vc acabou de digitar o número {n}!')
