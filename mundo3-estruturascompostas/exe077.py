words = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')
vogais = ''
for w in words:
    print(f'\nNa palavra {w.upper()} temos ', end='')
    for l in w:
        if l.lower() in 'aeiou':
            print(l, end=' ')
