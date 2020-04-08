import random
from time import sleep
cores = {'limpa':'\033[m', 'cinza':'\033[1;37m', 'azul':'\033[1;34m', 'verde':'\033[1;32m', 'roxo':'\033[1;35m'}
lista = ['Pedra', 'Papel', 'Tesoura']
choicePc = random.choice(lista).lower()

print('=:'*50)
print('   {}Bem-vindo ao nosso popular jogo ->JOKENPO. Aqui seu adiversário será o computador. Boa sorte!{}'.format(cores['azul'], cores['limpa']))
print('=:'*50)
userChoice = str(input('Digite {}pedra{} para escolher pedra.'
                       '\nDigite {}papel{} para papel.'
                       '\nDigite {}tesoura{} para escolher tesoura.'
                       '\n: '.format(cores['cinza'], cores['limpa'], cores['azul'], cores['limpa'], cores['verde'], cores['limpa'])))
userChoice = userChoice.lower()
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
print('Voce jogou e escolheu {}{}{}'.format(cores['roxo'], userChoice, cores['limpa']))
print('Computador jogou e escolheu {}{}{}'.format(cores['roxo'], choicePc, cores['limpa']))
if 'pedra' in userChoice or 'papel' in userChoice or 'tesoura' in userChoice:
    if 'pedra' in userChoice and 'tesoura' in choicePc:
        print('Parabéns, usuário! Você ganhou!!')
    elif 'pedra' in userChoice and 'papel' in choicePc:
        print('Que pena! Você perdeu. :(')
    elif 'pedra' in userChoice and 'pedra' in choicePc:
        print('Que coincidência! Vocês escolheram o mesmo e isso é um EMPATE!')
    elif 'papel' in userChoice and 'pedra' in choicePc:
        print('Parabéns, usuário! Você ganhou!!')
    elif 'papel' in userChoice and 'tesoura' in choicePc:
        print('Que pena! Você perdeu. :(')
    elif 'papel' in userChoice and 'papel' in choicePc:
        print('Que coincidência! Vocês escolheram o mesmo e isso é um EMPATE!')
    elif 'tesoura' in userChoice and 'papel' in choicePc:
        print('Parabéns, usuário! Você ganhou!!')
    elif 'tesoura' in userChoice and 'pedra' in choicePc:
        print('Que pena! Você perdeu. :(')
    elif 'tesoura' in userChoice and 'tesoura' in choicePc:
        print('Que coincidência! Vocês escolheram o mesmo e isso é um EMPATE!')
else:
    print('\033[31mOpção inválida! Tente novamente, por favor.\033[m')




