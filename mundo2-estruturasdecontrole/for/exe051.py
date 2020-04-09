print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao
print(decimo)
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('FINISHED')
