def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('ERRO: por favor, digite um número inteiro válido!')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário!')
        else:
            return n
            break


def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido!')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário!')
        else:
            return n
            break


num = leiaint('Digite um valor inteiro: ')
num2 = leiareal('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num}')
print(f'O valor real digitado foi {num2}')

