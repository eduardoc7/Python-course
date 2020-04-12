n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

if n1 > n2:
    maiornum = n1
    print('O maior número entre {} e {} é {}'.format(n1,n2,maiornum))
elif n2 > n1:
    maiornum = n2
    print('O maior número entre {} e {} é {}'.format(n1, n2, maiornum))
elif n1 == n2:
    print('Não existe maior número. Eles são iguais.')

