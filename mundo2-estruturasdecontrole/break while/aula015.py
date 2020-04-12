n = s = 0
while True:
    n = int(input('Digite um numero: '))
    s += n
    if n == 999:
        break
#print('A soma vale: {}'.format(s))
#fstrings
print(f'A soma vale {s}')
nome = 'Eduardo'
print(f'O {nome:^20} é legal as vezes!')
#{nome:-^20}centralziar e complementar
#{nome:->20}alinhar a direita e complementar
#{nome:-<20}alinhar a esquerda e complementar



