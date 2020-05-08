# dicionários são um tipo de variável composta, que possue um grande diferencial comparado as outras como tuplas e listas
# os dicionários podem ser acessados por índices literais
# são imutáveis
# é possível existir uma lista com vários dicícionarios (uma lista de objetos)
pessoas = {
    'nome': 'Eduardo',
    'sexo': 'M',
    'idade': 19
}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) # método para listar as palavras chaves do dicícionario
print(pessoas.items()) # método para buscar a composição de elementos trazendo a key e o value do dicionário
print(pessoas.values()) # método utilizado para trazer o conteúdo das keys do dicionário

pessoas['peso'] = 15156 # adicionar um vlaor no objeto
pessoas['nome'] = 'DUDUDUDU' # alterar o valor de um elemento
del pessoas['sexo'] # deletar um elemento

# podemos utilizar os três métodos em laços de repetição como por exemplo o for:
for k, v in pessoas.items():
    print(k, v)
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

