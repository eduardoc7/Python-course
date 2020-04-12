from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input(''' 
SELECIONE O QUE VOCE DESEJA FAZER COM OS VALORES:
[1] para somar
[2] para multiplicar
[3] para maior
[4] para digitar novos valores
[5] para sair do programa
--> '''))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1,num2,soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1,num2,mult))
    elif opcao == 3:
        maior = num1
        if num2 > num1:
            maior = num2
        print('O maior valor de {} e {} é {}'.format(num1,num2,maior))
    elif opcao == 4:
        num1 = int(input('Digite um primeiro novo valor: '))
        num2 = int(input('Digite um segundo novo valor: '))
print('\033[1;31mPrograma será encerrado em 3...')
(sleep(1))
print('Programa será encerrado em 2...')
(sleep(1))
print('Programa será encerrado em 1...\033[m')


