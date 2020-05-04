numbers = list()
opcao = ''
while True:
    num = int(input('Digite um valor para adicionar: '))
    if num not in numbers:
        numbers.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if 'N' in opcao:
        break
numbers.sort(reverse=True)
print(f'Voce digitou os valores {numbers}')
