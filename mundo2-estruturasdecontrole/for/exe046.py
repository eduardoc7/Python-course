from time import sleep
import emoji
print('='*80)
print('  Bem-vindo ao nosos programa de contagem regressiva (a contagem inicia-se em 0)')
print('='*80)
count = int(input('Digite um número que você deseja que contagem acabe: '))

for c in range(count, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('FELIZ NATAL!!! :tada: :boom: :fire: :star:', use_aliases=True))