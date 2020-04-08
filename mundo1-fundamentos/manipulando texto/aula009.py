frase = 'Curso em video python'
'''print(frase[:21])
print(frase[::1])
print(frase[5::2])'''
print("""#: é utilizado para fazer o fatiamento dentro da cadeia de texto, ::: -> o primeiro espaço é o inicio, o segundo é o fim e o terceiro é o salto.
#se não tiver nada entre os dois pontos significa que: começará no 0 terminará no ultimo valor do indice e pulará 1 em 1.
#o python sempre contará até um intervalo e não mostrará o o que há dentro do intervalo, por isso sempre coloque 1 a mais no indice da string.
#print(frase.count('o',0,13)) #utilizado para contar quantos caracteres há no cadeia de texto, entre o intervalo 0 e 13
#-1 significa que não foi encontrado nenhuma string dentro da cadeia
print(frase.find('aaaaaaaaa'))#mostra em qual posição do indice o caractere foi encontrado
print('Curso'in frase)#é um operador que verifica se existe a palavra dentro (in) da variável que no caso é frase. Se sim: True.
#por padrão não é possível transformar uma cadeia de caracteres, por ela ser imutável. Entretanto, é possível fazer isso utlizando métodos
#métodos de transformação: replace, upper, lower, capitalize, title(todas as palavras com a primeira letra maiuscula)
#frase.strip(): remover todos os espaços inuteis no inicio e no final da cadeia de texto.
#frase.rstrip():variação r, utilizado em alguns métodos - significa right
#frase.lstrip():variação l, utilizado em alguns métodos - significa left""")

#métodos de divisão
#frase.split(): cria uma divisão entre algum determinado intervalo das palavras, criando uma indexação nova
    #vai criar uma lista por padrão entre as palavras da cadeia de texto, onde cada elemento vai ser separado entre 0,1,2,3
#metódo de junção
#'-'join(frase): juntar todos os elementos de frase, utilizando o separador '-'
print(frase.replace('Curso','Android'))#replace significa substituir, ela substitui de uma forma secundária e não diretamente. a segunda palavra pela primeira
