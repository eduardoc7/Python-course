qtdPessoas = int(input('Digite a quantidade de pessoas para ver o maior e menor peso: '))
maiorpeso = 0
menorpeso = 0


for c in range(1, qtdPessoas+1):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso entre todoas as pessoas é: {} \nO menor peso é: {}'.format(maiorpeso,menorpeso))