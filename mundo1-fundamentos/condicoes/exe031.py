dist = float(input('Digite a distância da viagem em km/h: '))
if dist < 200:
    dist = dist*0.50
    print('Como a sua viagem é menor do que 200km/h \nVocê pagará R${}!'.format(dist))
else:
    dist = dist*0.45
    print('Como a sua viagem é maior do que 200km/h \nVocê pagará R${}!'.format(dist))