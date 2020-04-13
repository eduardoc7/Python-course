import math
print('-' * 30)
print('{:^30}'.format('WELCOME TO OUR BANK'))
print('-' * 30)
saque = int(input('Value for withdrawal: '))
total = saque
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
