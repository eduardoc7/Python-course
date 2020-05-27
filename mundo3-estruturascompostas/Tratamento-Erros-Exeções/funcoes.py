def menu_principal():
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)
    op = int(input('Sua opção: '))

    if op == 1:
        ver_pessoas()
    elif op == 2:
        nome = str(input('Nome: ') + '\n')
        idade = str(input('Idade: ') + '\n')
        cadastrar(nome, idade)
    elif op == 3:
        print('sair')


def ver_pessoas():
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)
    with open('testing.txt', 'r') as file:
        file.seek(0)
        list = file.readlines()
        print(list)
        for linha in list:
            print(linha)
        # se a posição da lista for impar é a idade se for par é o nome

    print('-' * 40)

def cadastrar(nome, idade):
    with open('testing.txt', 'a+') as file:
        file.write(nome)
        file.write(idade)

