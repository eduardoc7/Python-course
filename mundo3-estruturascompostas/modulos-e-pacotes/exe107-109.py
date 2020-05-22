from exe109 import moeda


p = float(input('Digite o preço: R$'))
print(f'A metade do preço {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro do preço {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% do preço {p} fica {moeda.aumentar(p, True)}')
print(f'Reduzindo 13% do preço {p} fica {moeda.reduzindo(p, True)}')