# mostrar calculadora na tela
print('-' * 40)
print("CALCULADORA v3.0 - DU")
print('-' * 40)
operacao = 0

# cria looping infinito. É parado no comando 'break'.
# eu acho que assim é mais simplificado e é mais atualizado também.
while True:
    # and nos inputs você pode fazer dessa forma, que é mais fácil e simplificada:
    # colocando o tipo da variável antes do int((input())
    num1 = int(input("Digite o primeiro número: "))
    operador = str(input("Digite o operador: (+,-,/,*) "))
    num2 = int(input("Digite o segundo número: "))

    # basicamnente o que eu mudei aqui foi alguns detalhes, mas a lógica do seu programa continua a mesma
    # eu removi a variavel operação, mas é porque eu achei mais viável assim.
    # também usei o elif ao invés de vários if's porque assim é melhor prática. basicamente é um 'senao se'
    # outra coisa que eu poderia ter feito, era criar validações pro usuário não digitar nenhum operador errado ou qualquer outra coisa errada, mas fica pra prox. tenho que jogar valorant
    # também usei o print(f''), que é uma meneira simplificada do python de fstrings
    # também eu mudei o '==' pra 'in' que é um recurso só da linguagem python, então é legal utilizar
    print(f'{num1} {operador} {num2} = ', end='') # o 'end' serve pra ele executar o print e continuar na mesma linha
                                                  # se vc perceber o num1, operador, num2 e o resultado estão na mesma linha
    # + soma
    if operador in '+':
        print(f'{num1 + num2}')
    # - subtração
    elif operador in '-':
        print(f'{num1 - num2}')
    # / divisão
    elif operador in '/':
        print(f'{num1 / num2}')
    # * multiplicação
    elif operador in '*':
        print(f'{num1 * num2}')

    teste = str(input("\nDeseja continuar calculando? digite [S/N]: "))
    if teste in 'Nn':
        break
print('FIM DO PROGRAMA!')
