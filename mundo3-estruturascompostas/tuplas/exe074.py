from random import randint
t = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for n in t:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(t)}')
print(f'O menor valor sorteado foi: {min(t)}')


