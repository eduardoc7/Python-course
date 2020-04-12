termo = int(input('Digite o termo da PA: ')) #onde começa
razao = int(input('Digite a razão da PA: ')) #o intervalo
                                              #exibir 10 vezes
i = 0; total = 0; opcao = 10;
while opcao != 0:
    total += opcao
    while i < total:
        print('{}'.format(termo), end=' ->')
        termo += razao
        i += 1
    print('PAUSA')
    opcao = int(input('Quantos termos voce quer ver a mais? [0 para sair]'))
print('O total de termos calculado foi {}'.format(total))
print('FIM')

