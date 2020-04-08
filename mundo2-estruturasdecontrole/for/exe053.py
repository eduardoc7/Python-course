frase = str(input('Digite um frase para o nosso programa verificar se é uma frase palíndroma: ')).strip().upper()
frase = frase.replace(' ','')
inverso = ''
for c in range(len(frase) -1, -1, -1 ):
    inverso += frase[c]
print('A frase {} ao INVERSO é {}.'.format(frase,inverso))
if frase == inverso:
    print('É PALINDROMO!')
else:
    print('NÃO É PALINDROMO!')




