import random


def recorde(vitorias, nome):
    print('-' * 40)
    print('RECORDES')
    print('-' * 40)


    vitorias = str(vitorias)
    datas['nome'] = nome
    datas['nvitoria'] = vitorias
    print(datas)

    # criar um dicionario para cada pessoa para listar pessoa e seu recorde
    # depois verificar qual pessoa tem a maior vitória
    # listar as 3 maiores


datas = dict()
datas['nome'] = 'teste'
datas['vit'] = '7'
with open('recordes.txt', 'r+') as file:
    tamanho = sum(1 for _ in file)
    print(tamanho)
    if tamanho <= 2:
        file.write(datas['nome'] + ' ' + datas['vit'] + '\n')
    else:
        file.seek(0)
        for linha in file.readlines():
            dados = linha.split()
            sorted(dados)
            print(dados)


# # Main Program
# cwin = num = tot = cont = 0; opcao = condicao = ''
# print('=-'*20)
# print(' '*6, '\033[1;35mVAMOS JOGAR PAR OU IMPAR\033[m')
# print('=-'*20)
# while True:
#     numPc = random.randint(0, 10)
#     if cont == 0:
#         nome = str(input('Digite seu nome: '))
#     num = int(input('Diga um valor: '))
#     opcao = str(input('Par ou Ímpar? [PAR/IMPAR] ')).upper()
#     tot = num+numPc
#     cont += 1
#     if tot % 2 == 0:
#         condicao = 'PAR'
#     else:
#         condicao = 'IMPAR'
#     if opcao == condicao:
#         print(f'Voce jogou {num} e o computador {numPc}. Total de: {tot} É \033[33m{condicao}\033[m!!')
#         print('\033[1;32mVOCÊ VENCEU!!\033[m')
#         cwin += 1
#     else:
#         print(f'Voce jogou {num} e o computador {numPc}. Total de: {tot} É \033[33m{condicao}\033[m')
#         print('\033[1;31mVOCÊ PERDEU!\033[m')
#         print('-' * 20)
#         print(f'Voce venceu \033[1;32m{cwin}\033[m vezes.')
#         recorde(cwin, nome)
#         break



