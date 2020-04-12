from random import randint
print('-'*50)
print('        Bem vindo ao programa de adivinha!')
print('-'*50)
print('\nAdivinhe o número entre 1 a 5 e ganhe do computador!')
num = int(input('Digite um numero: '))
num2 = randint(1,5)

numerotentativas = 1
while(num != num2):
    if num > num2:
        print('Seu palpite está alto!')
    elif num < num2:
        print('Seu palpite está baixo!')
    numerotentativas = numerotentativas + 1
    num = int(input('Tente outro valor: '))
    if numerotentativas >= 4:
        break
if numerotentativas == 4:
    print('Numero de tentativas acabaram!')
elif num == num2:
    print('Voce ganhou!')