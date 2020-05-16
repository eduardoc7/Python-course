from random import randint
from time import sleep
lista = list()


def sortea():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(1, 9)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.3)
    print('READY!')


def somapar():
    print(f'Somando os valores pares da lista {lista}, temos: ', end='')
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'{soma} ')


# Main Program
sortea()
somapar()
