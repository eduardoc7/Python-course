# alldatas = list()
# temp1 = list()
# temp2 = list()
# while True:
#     temp1.append(str(input('Nome: ')))
#     temp2.append(float(input('Nota1: ')))
#     temp2.append(float(input('Nota2: ')))
#     media = (temp2[0] + temp2[1]) / 2
#     temp2.append(media)
#     temp1.append(temp2[:])
#     temp2.clear()
#     alldatas.append(temp1[:])
#     temp1.clear()
#     opcao = str(input('Quer continuar? [S/N] '))
#     if opcao in 'Nn':
#         break
# for i, v in enumerate(alldatas):
#     print(f'{i} - {v[0]} - ', end=' ')
# for m in alldatas:
#     print(m[1][1])
# while True:

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f'{"ID":<4}{"NOME:":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Digite o ID do aluno para mostrar as notas [999 interrompe] '))
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    if opc == 999:
        break



