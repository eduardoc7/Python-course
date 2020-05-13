from time import sleep
nums = list()
opcao = ''


def maior(* args):
    print('-=' * 40)
    print('Analisando os valores passados...')
    for valor in args:
        print(f'{valor} ', end='')
    print(f'Foram informados {len(args)} valores ao todo.')
    print(f'O maior valor informado foi {max(args)}')


while True:
    nums.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar? '))
    if opcao in 'Nn':
        break
maior(* nums)

