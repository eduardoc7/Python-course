from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
agora = date.today()
idade = agora.year - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')