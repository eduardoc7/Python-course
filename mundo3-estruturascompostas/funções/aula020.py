# funções são blocos de código que realizam determinadas tarefas que normalmente precisam ser executadas diversas vezes dentro de uma aplicação.
# em várias linguagens de programação já possuem funções built-in nos seus programas, por exemplo, print em python.
# entretanto, pode ser que tenhamos a necessidade de criar funções personalizadas para executar uma rotina que fazemos com frequência.
# o objetivo da função é facilitar o código, eliminando a repetição de rotinas
# criando rotinas otimizadas, que serão executadas em qualquer lugar do programa quando chamadas.

# Um conjunto de parâmetros consiste em uma lista com nenhum ou mais elementos que podem ser obrigatórios ou opcionais.
# Para um parâmetro ser opcional atribuímos um valor padrão (default) para ele -
# o mais comum é utilizar None: def dados (nome, idade=None):
# def dados(nome, idade=None):
#     print('nome: {}'.format(nome))
#     if (idade is not None):
#         print('idade: {}'.format(idade))
#     else:
#         print('idade: não informada')
# fonte: https://www.caelum.com.br/apostila-python-orientacao-objetos/funcoes/#retornando-mltiplos-valores


# Função soma
def soma(a, b):
    print(a + b)


# Desempacotamento de argumentos
def contador(* args):
    for valor in args:
        print(f'{valor*2} ', end='')
    print('fim!')


# ** KWARGS permite que passemos o tamanho variável da palavra-chave dos argumentos para uma função
def minhaFunção(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


# Main program
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)

# empacotamento de funções:
# contador(2, 1, 7)
# contador(8, 0)
lista = [5, 5, 6, 7, 9]
contador(*lista)

# **kwargs
minhaFunção(nome='Eduardo', idade='20')

