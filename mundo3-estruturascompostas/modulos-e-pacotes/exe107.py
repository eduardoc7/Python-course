from exercicios import moeda


p = float(input('Digite o preço: R$'))
print(f'A metade do preço {p:.2f} é {moeda.metade(p):.2f}')
print(f'O dobro do preço {p:.2f} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10% do preço {p:.2f} fica {moeda.aumentar(p):.2f}')
print(f'Reduzindo 13% do preço {p:.2f} fica {moeda.reduzindo(p):.2f}')