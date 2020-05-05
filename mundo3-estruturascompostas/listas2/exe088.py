from random import randint
from time import sleep
sorteio = list()
temp = list()
print('-' * 50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-' * 50)
qjogos = int(input('Digite a quantidade de jogos a serem sorteados: '))
i = 1
while i <= qjogos:
    while len(temp) <= 5:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
    temp.sort()
    sorteio.append(temp[:])
    temp.clear()
    i += 1
print('-=' * 3, f' Sorteando {qjogos} jogos ', '-=' * 3)
for i, v in enumerate(sorteio):
    print(f'Jogo {i+1}: {v}')
    sleep(0.5)



