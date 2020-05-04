numbers = list()
pares = list()
impares = list()

while True:
    opcao = ''
    numbers.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if 'N' in opcao:
        break
for valor in numbers:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'A lista completa é {numbers}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
