velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('Voce foi multado! O valor da multa é {}'.format(multa))
else:
    print('Velocidade OK!')