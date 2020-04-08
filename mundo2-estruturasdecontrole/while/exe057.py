sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo not in 'FfMm':
    print('Sexo inválido! Digite novamente!')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
if sexo == 'M':
    print('Seu sexo é masculino!')
elif sexo == 'F':
    print('Seu sexo é feminino!')