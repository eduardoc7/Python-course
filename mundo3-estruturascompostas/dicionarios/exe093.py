datas = dict()
total = 0
datas['nome'] = str(input('Nome: '))
partidas = int(input('Quantas partidas ele jogou? '))
datas['gols'] = list()
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c+1}? '))
    total += gols
    datas['gols'].append(gols)

datas['total'] = total
print('-=' * 30)
print(datas)
print('-=' * 30)
print(f'O {datas["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(datas['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {total} goals!')


