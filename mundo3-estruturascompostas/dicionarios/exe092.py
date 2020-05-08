from datetime import datetime
datas = dict()

datas['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
datas['idade'] = datetime.now().year - anoNascimento
datas['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if datas['ctps'] != 0:
    datas['contratação'] = str(input('Ano de contratação: '))
    datas['salário'] = float(input('Salário: R$'))
    datas['aposentadoria'] = datas['idade'] + ((datas['contratação'] + 35) - datetime.now().year)
for k, v in datas.items():
    print(f'{k} tem o valor {v}')

