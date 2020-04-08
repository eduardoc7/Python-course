#estrutura de repetição com teste lógico
r = 'S'
while r == 'S':#condição de parada
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    n += 1
print('FIM')

n = 1; par = 0; impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar =+ 1
print('Voce digitou {} pares e {} imapres'.format(par, impar))