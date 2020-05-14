def calculadora(x, y):
    return{'soma': x + y, 'subtração': x - y, 'multiplicação': x * y, 'divisão': x / y}


cores = {'limpa': '\033[m', 'vermelho': '\033[1;31m', 'ciano': '\033[1;36m'}

# Main Program
print('-' * 47)
print(f'{cores["ciano"]}{"BEM VINDO A CALCULADORA MAIS SIMPLES DO BRASIL!"}{cores["limpa"]}')
print('-' * 47)
while True:
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    while True:
        opcao = str(input('Digite o que deseja fazer: '
                          f'\n{cores["vermelho"]}>soma<{cores["limpa"]} para somar'
                          f'\n{cores["vermelho"]}>subtração<{cores["limpa"]} para subtrair'
                          f'\n{cores["vermelho"]}>multiplicação<{cores["limpa"]} para multiplicar'
                          f'\n{cores["vermelho"]}>divisão<{cores["limpa"]} para dividir<'
                          f'\n=>  '))
        if 'soma' in opcao or 'subtração' in opcao or 'multiplicação' in opcao or 'divisão' in opcao:
            break
        print(f'Opção inválida! Por favor, tente novamente!')
    resultado = calculadora(x, y)
    print(f'A {opcao} entre {x} e {y} é igual a {resultado[opcao]}')
    sair = str(input('Deseja continuar? [S/N] '))
    if sair in 'Nn':
        break
print('<<< PROGRAMA ENCERRADO >>>')
