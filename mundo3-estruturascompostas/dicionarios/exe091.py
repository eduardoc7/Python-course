from random import randint
from time import sleep
from operator import itemgetter
datas = dict()
ranking = list()

for c in range(0, 4):
    datas[f'jogador{c+1}'] = randint(1, 6)
print('Valores Sorteados:')
for k, v in datas.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(0.5)
print('Ranking dos jogadores:')
ranking = sorted(datas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(0.5)

