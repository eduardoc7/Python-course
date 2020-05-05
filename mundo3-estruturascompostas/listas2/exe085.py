allnumbers = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}o valor: '))
    if num % 2 == 0:
        allnumbers[0].append(num)
    else:
        allnumbers[1].append(num)
allnumbers[0].sort()
allnumbers[1].sort()
print(f'Os valores pares digitados foram: {allnumbers[0]}')
print(f'Os valores pares digitados foram: {allnumbers[1]}')
