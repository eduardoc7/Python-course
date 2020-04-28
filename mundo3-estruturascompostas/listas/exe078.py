numbers = list()
for c in range(0, 5):
    numbers.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {numbers}')
print(f'O maior valor digitado foi {max(numbers)} nas posições ', end='')
for i, v in enumerate(numbers):
    if v == max(numbers):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(numbers)} nas posições ', end='')
for i, v in enumerate(numbers):
    if v == min(numbers):
        print(f'{i}... ')