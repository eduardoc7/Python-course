l1 = float(input('Digite o 1° lado: '))
l2 = float(input('Digite o 2° lado: '))
l3 = float(input('Digite o 3° lado: '))
#regra matemática: o valor de um lado tem que ser menor do que a soma entre os outros dois lados
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('É possível formar um triângulo!!')
else:
    print('Não é possível formar um triângulo!!')