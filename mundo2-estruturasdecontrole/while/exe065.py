print('Bem-vindo ao nosso programa para saber: \nO maior número \nO menor número \nE a media de todos digitados\n')
cont = 0; media = 0; num = 0; maiorNum = 0; menorNum = 0;opcao = ''
while 'N' not in opcao:
    num = int(input('Digite um número qualquer: '))
    if cont == 1:
        maiorNum = num
        menorNum = num
    if num > maiorNum:
        maiorNum = num
    elif num < menorNum:
        menorNum = num
    media += num
    cont += 1
    opcao = str(input('Deseja digitar outro? [S / N] ')).upper()
print('A média entre os valores é {} \nO maior número é {} \nO menor número é {}'.format(media / cont, maiorNum, menorNum))

