def leia_dinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO! "{entrada}" é um valor inválido!\033[m')
        else:
            ok = True
            return float(entrada)