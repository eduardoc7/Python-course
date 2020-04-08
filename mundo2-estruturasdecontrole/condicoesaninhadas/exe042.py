l1 = float(input('Digite 1° lado: '))
l2 = float(input('Digite 2° lado: '))
l3 = float(input('Digite 3° lado: '))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    if l1 == l2 and l2 == l3:
        print('É possível formar um triângulo com essas medidas e ele é EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('É possível formar um triângulo com essas medidas e ele é ISÓSCELES!')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('É possível formar um triângulo com essas medidas e ele é ESCALENO')
else:
    print('Não é possível formar um triângulo com essas medidas!')

