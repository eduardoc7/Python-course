jogador1 = int(input('Jogador1: Selecione 1 para pedra. 2 para tesoura. 3 para papel.'))
jogador2 = int(input('Jogador2: Selecione 1 para pedra. 2 para tesoura. 3 para papel.'))

if jogador1 == 1 and jogador2 == 1:
    print('Empate!')
elif jogador1 == 1 and jogador2 == 3:
    print('Jogador 2 venceu!')
elif jogador1 == 1 and jogador2 == 2:
    print('Jogador 1 venceu!')
elif jogador1 == 2 and jogador2 == 1:
    print('Jogador 2 venceu!')
elif jogador1 == 2 and jogador2 == 2:
    print('Emapte!')
elif jogador == 2 and jogador2 == 3:
    print('Jogador 1 venceu!')
elif jogador1 == 3 and jogador2 == 3:
    print('Empate!')
elif jogador1 == 3 and jogador2 == 1:
    print('Jogador 1 venceu!')
elif jogador1 == 3 and jogador2 == 2:
    print()
