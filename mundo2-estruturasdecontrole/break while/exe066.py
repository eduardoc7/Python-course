c = sum = num = 0
while True:
    num = int(input('Digite um número para somar (999 parar o programa): '))
    if num != 999:
        sum += num
        c += 1
    else:
        break
print(f'A soma dos {c} valores foi {sum}')