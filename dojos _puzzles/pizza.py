from time import sleep
pizzas = list()
sabores = dict()
datas = dict()
mediam = mediaqq = mediafc = 0

print('-' * 60)
print(f'{"BEM VINDO AO NOSSO PROGRAMA PARA ESCOLHER SOBORES DE PIZZAS":^60}')
print('-' * 60)
qpessoas = int(input('Digite quantas pessoas participarão da votação: '))

for c in range(0, qpessoas):
    datas['nome'] = str(input(f'Nome da pessoa {c+1}: '))
    sleep(0.2)
    print('Agora, vamos registrar as notas das pizzas! (digite um valor de 0 a 5).')
    datas['sabores'] = list()
    sabores['marguerita'] = float(input('Nota para pizza MARGUERITA: '))
    mediam += sabores['marguerita']
    sabores['quatro queijos'] = float(input('Nota para pizza QUATRO QUEIJOS: '))
    mediaqq += sabores['quatro queijos']
    sabores['frango com catupiry'] = float(input('Nota para pizza FRANGO COM CATUPIRY: '))
    mediafc += sabores['frango com catupiry']
    print(f'{datas["nome"]} votou com sucesso, com as seguintes notas: ')
    for k, v in sabores.items():
        print(f'{k}: {v}')
    datas['sabores'].append(sabores.copy())
    pizzas.append(datas.copy())
    sleep(1)
print('-' * 60)
print(f'A média do sabor MARGUERITA É: {mediam / len(pizzas)}')
print(f'A média do sabor QUATRO QUEIJOS É: {mediaqq / len(pizzas)}')
print(f'A média do sabor FRANGO COM CATUPIRY É: {mediafc / len(pizzas)}')
print('-' * 60)
print('PESSOAS QUE VOTARAM:')
print()
print(f'    {"ID":<5} {"NOME":<10}')
print('-' * 60)
for i, v in enumerate(pizzas):
    print(f'    {i:<5}', end='')
    print(f'{v["nome"]:<10}', end='')
    print()
print('-' * 60)
while True:
    busca = int(input('\nMostrar notas de qual pessoa? (999 para encerrar) '))
    if busca == 999:
        break
    if busca >= len(pizzas):
        print(f'Erro! Não existe ninguém com o código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DAS NOTAS DO {pizzas[busca]["nome"]} --- ')
        for v in pizzas[busca]['sabores']:
            for k, d in v.items():
                print(f'Para o sabor {k} votou com a nota {d}.')
            print()
print('-' * 60)
for c in range(3, 0, -1):
    print(f'Programa encerrando em {c}')
    sleep(0.5)



