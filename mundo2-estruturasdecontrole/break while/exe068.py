import random



def recorde(vitorias, nome):
    print('-' * 40)
    print('RECORDES')
    print('-' * 40)
    recordes = list()
    recordes.append(vitorias)

    # criar um dicionario para cada pessoa para listar pessoa e seu recorde
    # depois verificar qual pessoa tem a maior vitória
    # listar as 3 maiores
    if len(recordes) <= 3:
        with open('recordes.txt', 'a+') as file:
            file.write(nome + ' ' + vitorias)


# Main Program
cwin = num = tot = 0; opcao = condicao = ''
print('=-'*20)
print(' '*6, '\033[1;35mVAMOS JOGAR PAR OU IMPAR\033[m')
print('=-'*20)
while True:
    numPc = random.randint(0, 10)
    nome = str(input('Digite seu nome: '))
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
        recorde(cwin, nome)
        break



