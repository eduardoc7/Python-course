# funções parte 2:
    # interactive help
    # docstrings
    # argumentos opcioanis
    # escopo de variáveis
    # retornos de resultados

# INTERACTIVE HELP - help()
    # abrir o python console e pesquisar pela função para abrir o manual. EXEMPLO: help(print)
    # mostrar informações sobre parametros ex: input.__doc__

# DOCSTRINGS
    # são os manuais que cada função possuem, por padrão nós podemos utilizar o help para mostrar os manuais do python.
    # o diferencial do docstring é que podemos criar manuais para as nossas funções personalizadas.
    # as docstrings por padrão começam logo após a linha de parametros da nossa função.
    # para criar uma docstring para uma função personalizada (criado por nós mesmos):
    # dentro da função: digite 3 as aspas duplas que o proprio python montará um modelo de docstring baseado na função atual
    # """ dsadsadsa """
    # para visualizar o manual: help(nomedafuncao)

# PARAMETROS OPCIONAIS
    # def somar(a = 0, b = 0, c=0):
    # neste exemplo acima, caso o parametro nao seja informado na chamada da função, ele seria 0.
    # tornando-o opcional

# ESCOPO DE VARIÁVEIS
    # variáveis criadas dentro de funções possuem um escopo local, como por exemplo, criadas dentro de for.
    # variáveis criadas fora das funções possuem um escopo global.
    # para alterar o valor de uma variável global dentro de um escopo local, ex: função
    # global a
    # a = 8
    # fazendo alterações na variável global do programa.

# RETORNO DE VALORES - (return)
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
# resultado1 = somar(3, 2, 5)
# resultado2 = somar(3, 5)
# print(f'Meus calculos deram {resultado1} e {resultado2}.')


# PARTE PRÁTICA
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        print(f)
    return f


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


num = int(input('Digite um número: '))
if par(num):
    print('PAR!')
else:
    print('IMPAR!')

