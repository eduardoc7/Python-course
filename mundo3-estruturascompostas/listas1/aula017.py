#append() adicionar um elemento no final da lista
#insert() adicionar um elemento em qualquer lugar da lista
#pop() deletar o ultimo elemento da lista
#remove() deleta um elemento indicando qual elemento
#sort() ordenar
#sort(reverse=True) ordernar inverso
#a = [2, 5, 6]
#b = a //faz uma ligação entra as lista
#b = a[:] faz uma cópia da lista a
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num = int(input('aaaa '))
bin = bin(num)
hex = hex(num)
print(bin)
print(hex)