matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3 = m2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > m2:
        m2 = matriz[1][c]
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 40)
print(f'A soma de todos os valores pares digitados foi {somap}')
print(f'A soma dos valores da terceira coluna foi {soma3}')
print(f'O maior valor da segunda linha é {m2}')
