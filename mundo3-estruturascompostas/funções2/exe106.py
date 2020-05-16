from time import sleep


def mostrarmanual():
    print('-=' * 20)
    print(f'{"SISTEMA DE AJUDA PYHELP":>31}')
    print('-=' * 20)
    busca = ''
    while 'fim' not in busca:
        busca = str(input('Função ou Biblioteca -> '))
        print('-=' * 20)
        print(f'{f"ACESSANDO O MANUAL DE AJUDA DO {busca}...":>31}')
        print('-=' * 20)
        sleep(2)
        help(busca)


mostrarmanual()
