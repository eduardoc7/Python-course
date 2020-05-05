pessoas = list()
dados = list()
opcao = ''
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg dos indivíduos', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg dos indivíduos ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')


