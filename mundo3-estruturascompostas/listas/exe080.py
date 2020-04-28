numbers = list()
maior = 0
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > numbers[-1]:
        numbers.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(numbers):
            if num <= numbers[pos]:
                numbers.insert(pos, num)
                print(f'Adicionado com sucesso na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados foram {numbers}')




