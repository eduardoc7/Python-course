from time import sleep


def cont(inicio, fim, passo):
    print('-=' * 40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    c = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        while c <= fim:
            print(f'{c} ', end='')
            sleep(0.3)
            c += passo
        print('FIM!')
    else:
        while c >= fim:
            print(f'{c} ', end='')
            sleep(0.3)
            c -= passo
        print('FIM!')


# Main Program
cont(1, 10, 1)
cont(10, 0, 2)
print('-=' * 40)
print('Agora é a sua vez de personalizar!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)
