datas = dict()

datas['Nome'] = str(input('Nome: '))
datas['Média'] = float(input(f'Média de {datas["Nome"]}: '))
datas['Situação'] = 'Aprovado' if datas['Média'] >= 7 else 'Reprovado'
for k, v in datas.items():
    print(f'{k} é igual a {v}')

