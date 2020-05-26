from uteis import numbers
# modularização = construir modulos
    # surgiu na década de 60 - implementações nas empresas
    # para suprir a necessidade de sistemas maiores
    # objetivo: dividir e organizar programas maiores em menores
    # objetivo2: melhorar a legibilidade
    # objetivo3: facilitar a manutenção
# vantagens:
    # organização do código
    # facilidade de manutenção
    # ocultação do código detalhado
    # reutilização em outros projetos

# pacotes = são grandes quantidade de módulos organizados em pastas e assuntos
    # também chamados de bibliotecas
    # no python/prjeto do pycharm toda pasta é considerado um pacote e pode servir para importação
    # cada pacote deve conter na sua pasta o arquivo __init__.py
    # um pacote pode conter outros pacotes dentro da sua pasta raiz ou simplesmente outros módulos

num = int(input('Digite um número: '))
fat = numbers.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numbers.dobro(num)}')