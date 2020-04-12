#estrutura aninhada: é quando voce tem uma condição dentro de outra condição
#sendo representada no python como elif(else if)
nome = str(input('Qual é o seu nome? '))
nome = nome.capitalize()
if nome == 'Eduardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))