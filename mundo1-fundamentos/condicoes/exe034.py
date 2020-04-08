salario = float(input('Digite seu salário: R$'))
if salario > 1250:
    aumento = (salario*10)/100
    aumento = aumento + salario
    print('Com o salário de {:.2f} e aumento de 10%. Voce terá um salário de {:.2f}'.format(salario,aumento))
else:
    aumento = (salario*15)/100
    aumento = aumento + salario
    print('Com o salário de {:.2f} e aumento de 15%. Voce terá um salário de {:.2f}'.format(salario, aumento))
