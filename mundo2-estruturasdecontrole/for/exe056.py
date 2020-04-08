mediaIdade = 0
maiorIdade = 0
totalMulheres = 0
oldMan = ''

for c in range(1, 4+1):
    nome = str(input('Digite o {}° nome: '.format(c))).upper()
    idade = int(input('Digite a idade do(a) {}: '.format(nome)))
    sexo = str(input('Digite o sexo M e F do(a) {}: '.format(nome)))
    mediaIdade += idade
    if c == 1 and sexo in "Mm":
        maiorIdade = idade
        oldMan = nome
    else:
        if idade > maiorIdade:
            maiorIdade = idade
            oldMan = nome
    if 'Ff' in sexo and idade < 20:
        totalMulheres += 1

print('A média do grupo é: {}'.format(mediaIdade / 4))
print('O nome do homem mais velho tem {} anos se chama {}'.format(maiorIdade,oldMan))
print('Quantidade de mulheres com menos de 20 anos é: {}'.format(totalMulheres))