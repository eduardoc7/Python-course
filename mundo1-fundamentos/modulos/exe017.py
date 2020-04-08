from math import hypot
'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2)**(1/2)
print('A hipotenusa é {:.2f}'.format(hi))'''
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi  = hypot(co,ca)
print('A hipotenusa é {:.2f}'.format(hi))



