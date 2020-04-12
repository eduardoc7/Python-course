from time import sleep
c = 1; num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    c = 1
    if num < 0:
        break
    while c < 11:
        print(f'{num} x {c} = {num*c}')
        c += 1
print('\033[1;31mPrograma tabuada será encerrado em 3...')
sleep(0.5)
print('Programa tabuada será encerrado em 2...')
sleep(0.5)
print('Programa tabuada será encerrado em 1...\033[m')
