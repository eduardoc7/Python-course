numero = int(input('Digite um núemro para conversão: '))
conversao = str(input('Digite bin para binário. \nDigite hex para hexadecimal. \nDigite oct para octal. \n: '))

if conversao == 'bin':
    print('O {} em decimal é {} em binário'.format(numero, bin(numero)[2:]))
elif conversao == 'hex':
    print('O {} em decimal é {} em hexadecimal'.format(numero, hex(numero)[2:]))
elif conversao == 'oct':
    print('O {} em decimal é {} em octal'.format(numero, oct(numero)[2:]))
else:
    print('Nome incorreto, por favor tente novamente!')

