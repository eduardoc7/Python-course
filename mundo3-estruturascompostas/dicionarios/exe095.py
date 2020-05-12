jogadores = list()
datas = dict()
opcao = ''
while True:
    datas['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    datas['goals'] = list()
    total = 0
    for c in range(0, partidas):
        goals = int(input(f'Quantos goals na partida {c+1}: '))
        total += goals
        datas['goals'].append(goals)
    datas['total'] = total
    jogadores.append(datas.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in datas.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Erro! não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['goals']):
            print(f'    No jogo {i+1} fez {g} goals.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')




