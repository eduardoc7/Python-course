num = int(input('Digite quantos termos voce deseja ver de Fibonacci: '))
i = 3; t1 = 0; t2 = 1; t3 = 0;
print('{} -> {}'.format(t1, t2), end='')
while i <= num:
    t3 = t1 + t2
    print(' ->{}'.format(t3), end='')
    t1 = t2
    t2 = t3
    i += 1
print(' ->FIM')
