peso = float(input('Digite seu peso: '))
altura  = float(input('Digite sua altura: '))

imc = peso / (altura*altura)

if imc <= 18.5:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Você está abaixo do peso! Por favor, liga agora para o nosso nutricionista especilista, tel: 555-555-555')
elif imc > 18.5 and imc < 25:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Você está no peso ideal, veremos até quanto tempo isso durará. hehe xd!')
elif imc > 25 and imc < 30:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Lamento info85rmar, você está na categoria de obesidade! Entretanto, não esqueça a felicidade está nas coisas simples!')
elif imc > 40:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Voce está na categoria de Obesidade Mórbida. Procure um método laboritorial para melhorar isso se te incomoda.')