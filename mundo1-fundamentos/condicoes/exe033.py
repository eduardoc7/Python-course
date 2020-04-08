n1: int = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
n3 = int(input('Digite o 3° numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n1 > n2 and n1 > n2:
    maior = n3
print('O menor número digitado é {}'.format(menor))
print('O maior número digitado é {}'.format(maior))
