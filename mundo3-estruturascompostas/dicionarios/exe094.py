pessoas = list()
datas = dict()
media = 0
while True:
    datas['nome'] = str(input('Nome: '))
    while True:
        datas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if datas['sexo'] in 'MF':
            break
        print('Sexo inválido! Digite apenas M ou F.')
    datas['idade'] = int(input('Idade: '))
    media += datas['idade']
    pessoas.append(datas.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('Opção inválida! Digite apenas S ou N.')
    if opcao == 'N':
        break
print(pessoas)
print('-=' * 30)
print(f' - O grupo tem {len(pessoas)} pessoas.')
print(f' - A média de idade é de {media / len(pessoas):5.2f} anos.')
print(f' - As mulheres cadastradas foram: ', end='')
for v in pessoas:
    if v['sexo'] == 'F':
        print(f'{v["nome"]}', end='')
    print()
print(f'\n - Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= (media / len(pessoas)):
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
