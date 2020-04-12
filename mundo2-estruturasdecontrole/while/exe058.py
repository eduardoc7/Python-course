from random import randint
pcNum = randint(0, 10)
userNum = int(input('Digite um número entre 0 e 10 para tentar adivinhar e ganhar do computador: '))
i = 0;
while userNum != pcNum:
    if userNum > pcNum:
        print('Seu palpite está muito alto!')
    elif userNum < pcNum:
        print('Seu palpite está muito baixo!')
    print('Tentativa incorreta!')
    userNum = int(input('Tente novamente outro valor: '))
    i += 1
print('PARABÉNS!!! Você acertou e ganhou do computador!')
print('Você utilizou {} tentativas para adivinhar!'.format(i))