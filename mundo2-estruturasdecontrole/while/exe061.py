termo = int(input('Digite o termo da PA: ')) #onde começa
razao = int(input('Digite a razão da PA: ')) #o intervalo
                                             #exibir 10 vezes
i = 0
while i < 10:
    print('{}'.format(termo), end=' ->')
    termo += razao
    i += 1
print('Finished')


