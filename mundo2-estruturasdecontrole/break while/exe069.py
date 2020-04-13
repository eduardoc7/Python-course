print('-'*25)
print(' '*3, 'REGISTER A PERSON')
print('-'*25)
age = demaior = homens = mulher20 = 0
while True:
    age = int(input('Age: '))
    sexo = ' '
    opcao = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if age > 18:
        demaior += 1
    elif sexo in 'M':
        homens += 1
    elif sexo in 'F' and age < 20:
        mulher20 += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao in 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {demaior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')
