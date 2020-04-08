from random import shuffle
a1 = str(input('Digite o 1° aluno: '))
a2 = str(input('Digite o 2° aluno: '))
a3 = str(input('Digite o 3° aluno: '))
a4 = str(input('Digite o 4° aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem da apresentação será:')
print(lista)