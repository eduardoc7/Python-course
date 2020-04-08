#CONDIÇÕES
#condição simplificada:
print('Carro novo'if tempo<=3 else 'Carro velho')

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Eduardo':
    print('Que nome lindo voce tem!')
else:
    print('Nome normal!')
print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')'''
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))
print('Aprovado'if m>=6 else 'Reprovado')

