import random
cwin = num = tot = 0; opcao = condicao = ''
print('=-'*20)
print(' '*6, '\033[1;35mVAMOS JOGAR PAR OU IMPAR\033[m')
print('=-'*20)
while True:
    numPc = random.randint(0, 10)
    num = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar? [PAR/IMPAR] ')).upper()
    tot = num+numPc
    if tot % 2 == 0:
        condicao = 'PAR'
    else:
        condicao = 'IMPAR'
    if opcao == condicao:
        print(f'Voce jogou {num} e o computador {numPc}. Total de: {tot} É \033[33m{condicao}\033[m!!')
        print('\033[1;32mVOCÊ VENCEU!!\033[m')
        cwin += 1
    else:
        print(f'Voce jogou {num} e o computador {numPc}. Total de: {tot} É \033[33m{condicao}\033[m')
        print('\033[1;31mVOCÊ PERDEU!\033[m')
        print('-' * 20)
        print(f'Voce venceu \033[1;32m{cwin}\033[m vezes.')
        break

