# Tratamento de Erros e Exeções

# Exeções: Uma exceção representa um comportamento anormal, indesejado, que ocorre raramente e requer alguma ação
# imediata, um tratamento adequado, em uma parte do programa. Uma exceção indica uma condição de erro, tal como um overflow
# aritmético, uma divisão por zero, uma referência a um objeto nulo. Uma exceção também pode indicar uma ocorrência anormal
# mas que não é considerada um erro, tal como o fim do arquivo.
# Comandos escritos da forma correta porém encontram uma forma inválida de execução
# Exemplo no Python: NameError, ValueError, ZeroDivisionError, IndexError, ModuleNotFoundError, KeyError, EOFError, OSError, MemoryError
# No python todas as exeções são filhos de uma classe maior chamada exception, que podemos utilizar para buscar informações sobre alguma exceção
# o try funciona, meio que: ao invés de eu mandar o programa ele fazer exatamente tal coisa, com o try ele primeiro vai tentar
# o objetivo é eliminar e personalizar os tipos de erros mais comuns
# Try:
#    'operação'
#   'O que geralmente daria problema'
#   'Qual o comando que normalmente dariam problemas'
# except:
    # area da falha, ou seja, se eu tentar a coisa do try, o que vai acontecer?
# else:
    # area se der certo o try
# finally:
    # será executado independente do resultado do try
    # opcional
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except Exception as erro:
    # colocando a exeção dentro de uma variável para ter acesso a classe e ao erro
    print('Infelizmente tivemos algum problema!')
    print(f'O problema encontrado foi {erro.__class__}') # retornar a classe do erro
    # 1 único try pode ter vários excepts
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
