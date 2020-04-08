pares = 0
for c in range(1, 7):
    num = int(input('Digite o {}° numero: '.format(c)))
    if num % 2 == 0:
        pares += num
print('A soma de todos os número pares é: {}. (os números impares foram desconsiderados)'.format(pares))