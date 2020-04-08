print('=>'*40)
print('\033[34mBem-vindo ao nosso programa de calcular empréstimos!\033[m')
print('=>'*40)
valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anosPagar = int(input('Digite em quantos anos você deseja pagar: '))

prestMensal = valorCasa/anosPagar*12
print(prestMensal)

if prestMensal < (salario*30)/100:
    print('\033[1;30;42mEmpréstimo aprovado!\033[m')
else:
    print('\033[1;30;41mEmpréstimo negado!\033[m')
