num = 0; soma = 0; cont = 0;
print('Digite vários números para saber sua soma \nDigite "999" para sair do programa!')
while num != 999:
    num = int(input('Digite um numero inteiro qualquer: '))
    if num != 999:
        cont += 1
        soma += num
    print('A soma dos números até então é {}'.format(soma))
print('Voce digitou {} números e a soma entre eles é {}'.format(cont, soma))


