from random import choice
a1 = str(input('Digite o 1° aluno: '))
a2 = str(input('Digite o 2° aluno: '))
a3 = str(input('Digite o 3° aluno: '))
a4 = str(input('Digite o 4° aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O escolhido foi: {}'.format(escolhido))



