from math import sqrt
#importação específica não é necessário utilizar o math.
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, raiz))