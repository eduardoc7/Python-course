num = int(input('Digite um número para saber seu fatorial.!'))
i = num; fatorial = 1
while i > 0:
    print('{}'.format(i), end=' ')
    print(' x ' if i > 1 else ' = ', end=' ')
    fatorial *= i
    i -= 1
print(fatorial)
#from math import factorial