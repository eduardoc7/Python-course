t = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))

print(f'Voce digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes.')
print(f'O valor 3 apareceu na {t.index(3)+1}° posição' if 3 in t else 'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for num in t:
    if num % 2 == 0:
       print(f'{num} ', end='')

