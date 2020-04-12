#código ansi é chamado no python e em outras linhagens com a contra barra "\"
#escape sequence: Código escape ANSI. Os códigos de escape ANSI utilizam-se para dar formato à saída de um terminal de texto e baseiam-se numa norma ANSI, ANSI X3.
#código para as cores que funciona melhor no python: \033[0;33;44m
#0: estilo da cor do terminal - none (nada). 1: bold - 4: underline - 7: negative
#33: estilo da cor do texto. Cores são entre 30 a 37 por padrão
#44: estilo da cor de fundo. Entre 40 e 47
#podem ser escritos em qualquer ordem
#biblioteca de cores disponível pro python - colorwize
print('\033[1;31;43mHello World!\033[m')
print('\033[4;30;45mHello World!\033[m')
print('\033[7;33;44mHello World!\033[m')
print('\033[7;33;44mHello World!\033[m')
a = 19
b = 15
nome = 'Eduardo'
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7;30m'}
print('Os valores são \033[33m{}\033[m e \033[35m{}\033[m'.format(a,b))
print('Olá, muito prazer. {}{}{}'.format('\033[4;33m', nome, '\033[m'))
print('Olá, muito prazer. {}{}{}'.format(cores['azul'], nome, cores['limpa']))
