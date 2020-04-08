from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))

agora = date.today()
idade = agora.year-nascimento
print('Quem nasceu em {} tem {} em {}.'.format(nascimento, idade, agora.year ))

if idade < 17:
    print('Você ainda precisa se alistar no exército!')
    print('Faltam {} anos para o seu alismento que será no ano de {}'.format((17-idade), nascimento+17))
elif idade == 17:
    print('Está no ano de se alistar, corra!')
elif idade >= 18:
    print('Voce já passou {} anos do tempo de alistamento.'.format(idade-17))

