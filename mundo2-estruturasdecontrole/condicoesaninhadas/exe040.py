n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media < 5.0:
    print('Reprovado diretamente!')
elif 7 > media >= 5:
    print('Se dedique para estudar na recuperação!')
elif media >= 7.0:
    print('Paranbéns!! Você está aprovado!')
