num = int(input('Digite um número inteiro para ver se ele é primo ou não: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[35m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('é primo')
else:
    print('nao é primo')
