# listas compostas - listas dentro de listas
# matrizes
# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:]) #copia da lista
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:]) #copia da lista
# print(galera)

peoples = list()
data = list()

for c in range(0, 2):
    data.append(str(input('Nome: ')))
    data.append(int(input('Idade: ')))
    peoples.append(data[:])
    data.clear()
for p in peoples:
    print(p)
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade')