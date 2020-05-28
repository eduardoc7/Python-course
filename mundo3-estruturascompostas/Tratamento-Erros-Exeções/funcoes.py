from time import sleep


def menu_principal():
    sleep(0.5)
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)
    try:
        op = int(input('Sua opção: '))
    except (ValueError, TypeError):
        print('ERRO: opcção inválida, tente novamente!')
    else:
        if op == 1:
            ver_pessoas()
        elif op == 2:
            nome = str(input('Nome: ') + '')
            idade = str(input('Idade: ') + '')
            cadastrar(nome, idade)
        elif op == 3:
            sair()
        else:
            print('ERRO: opcção inválida, tente novamente!')


def ver_pessoas():
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)
    with open('testing.txt', 'r') as file:
        print(f'\33[30;1m{"NOME":<34}{"IDADE":^6}\n\33[m')
        for linha in file.readlines():
            dados = linha.split()
            nome = ' '.join(dados[:-1])
            idade = dados[-1]
            print(f'\33[30m{nome:<34}{idade:^6}\33[m')
    menu_principal()


def cadastrar(nome, idade):
    with open('testing.txt', 'a+') as file:
        file.write(nome + ' ' + idade + '\n')


def sair():
    print('Encerrando o programa em 3...')
    sleep(0.5)
    print('Encerrando o programa em 2...')
    sleep(0.5)
    print('Encerrando o programa em 1...')
    sleep(0.5)
    exit()



