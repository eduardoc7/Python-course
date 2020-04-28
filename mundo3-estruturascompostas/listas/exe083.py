expressoes = list()
num = str(input('Digite uma expressão matemática: '))
expressoes.append(num)
cont = 0
for numero in expressoes:
    for parenteses in numero:
        if '(' in parenteses or ')' in parenteses:
            cont += 1
if cont % 2 == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')