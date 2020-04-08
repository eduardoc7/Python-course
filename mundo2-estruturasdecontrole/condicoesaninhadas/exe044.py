cores = {'limpa': '\033[m', 'pagamento': '\033[36m', 'title': '\033[1;34m'}
print('>/' * 50)
print(' ' * 30, '{}Bem-vindo ao nosso sistema de pagamento{}'.format(cores['title'], cores['limpa']))
print('>/' * 50)
valorProduto = float(input('Digite o valor do produto: R$'))
formaPagamento = str(input('Agora selecione a forma de pagamento:\nÀ vista: Digite {}vis{}'
                           '\nÀ vista no cartão: Digite {}viscard{}'
                           '\n2x no cartão: Digite {}2x{}'
                           '\n3x ou mais no cartão: Digite {}3x{}'
                           '\n: '.format(cores['pagamento'], cores['limpa'], cores['pagamento'], cores['limpa'],
                                         cores['pagamento'], cores['limpa'], cores['pagamento'], cores['limpa'])))

if 'vis' in formaPagamento or 'viscard' in formaPagamento or '2x' in formaPagamento or '3x' in formaPagamento:
    if 'vis' in formaPagamento:
        print('Muito bem, você escolheu a forma de pagamento a vista no dinheiro e ganhou 10% de desconto.')
        print('Seu produto de R${:.2f} foi para R${:.2f}'.format(valorProduto, (valorProduto*10)/100+valorProduto))
    elif 'viscard' in formaPagamento:
        print('Muito bem, você escolheu a forma de pagamento a vista no cartão e ganhou 5% de desconto.')
        print('Seu produto de R${:.2f} foi para R${:.2f}'.format(valorProduto, (valorProduto * 5) / 100+valorProduto))
    elif '2x' in formaPagamento:
        print('Muito bem, você escolheu a forma de pagamento em até 2x no cartão e o preço do produto será normal, sem desconto =/.')
        print('Preço do produto: R${:.2f}'.format(valorProduto))
    elif '3' in formaPagamento:
        print('Muito bem, você escolheu a forma de pagamento de 3x ou mais no cartão, então você pagará 20% de juros no produto de R${}'.format(valorProduto))
        juros = (valorProduto * 20)/100
        print('O seu produto de R${:.2f} foi para R${:.2f}'.format(valorProduto,valorProduto+juros))
else:
    print('Digite uma forma de pagamento válida e tente novamente!')
