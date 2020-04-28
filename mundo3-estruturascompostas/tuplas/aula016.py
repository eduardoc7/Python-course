#VARIÁVEIS COMPOSTAS - TUPLAS
#existem tres tipos no python, tuplas, listas e dicíonarios
#Tuplas: uma variável que armazena mais de um valor
#as tuplas são imutáveis
#as tuplas no python, diferente de outras linguagens aceitam diferentes tipos de variaveis em apenas uma
pessoas = ('Eduardo', 19, 'M')
lanche = ('Hambuerguer', 'Suco', 'Pizza', 'Pudim')
#juntando tuplas
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
print(c.count(5))#para contar quantas vezes existe um valor dentro da tupla
print(c.index(5))#para buscar em qual posição está localizado um valor dentro da tupla
print(sorted(lanche)) #organizar por ordem alfabética
for position, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {position}')
print('Comi demais!')

#deletar os valores das tuplas armazenados na memória ou qualquer outra variaǘel dentro do python
del(pessoas)