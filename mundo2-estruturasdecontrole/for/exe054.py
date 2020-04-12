from datetime import date
qtdPessoas = int(input('Digite a quantidade de pessoas para verificar a maioridade: '))
anoNasc = []
agora = date.today()
idade = 0
maiores = 0
naomaiores = 0
for c in range(0, qtdPessoas):
    anoNasc.append(int(input('Digite o ano de nascimento da {}° pessoa: '.format(c+1))))
    idade = agora.year - anoNasc[c]
    if idade >= 21:
        print('Você já atingiu a maioridade!')
        maiores += 1
    else:
        print('Você ainda não atingiu a maioridade!')
        naomaiores += 1
print('O número de pessoas da nossa lista que ja atingiram a maioridade é: {} \nE o número de pessoas que ainda não atingiram é: {}'.format(maiores,naomaiores))


