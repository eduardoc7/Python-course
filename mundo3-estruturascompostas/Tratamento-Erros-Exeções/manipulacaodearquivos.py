# https://docs.python.org/3/library/functions.html#open
file =open('testing.txt', 'w+')# abrir o arquivo, com o parametro w+ para leitura e escrita
file.write('linha 1 \n')# escrever no arquivo
file.write('linha 2 \n')# escrever no arquivo

file.seek(0, 0)# o cursor do python ira lendo o arquivo linha por linha e aqui neste momento estariamos na linha 3, para listar mandamos o cursos com o metodo seek para o inicio
print('lendo linhas:')
print(file.read())# ler linhas
# com o readlines, utilizar o end para nao quebrar 2 linhas

file.seek(0, 0)
# conteudo = file.readlines()
for linha in file:
    print(linha, end='')
file.close()# fechar o arquivo, utilizado após todas as mudanças no arquivo.

# melhor maneira de abrir arquivos e trabalhar no python (serve para outras coisas além de arquivos)
with open('testing.txt', 'w+') as file:# a+ append mode, adicionar sem apagar
    file.write('linha1')


