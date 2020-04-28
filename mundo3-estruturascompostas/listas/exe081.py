numbers = list()
opcao = ''
cont = 0
while 'N' not in opcao:
    numbers.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
numbers.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {numbers}')
for pos, v in enumerate(numbers):
    if v == 5:
        print(f'O valor 5 foi encontrado na posição {pos}!')