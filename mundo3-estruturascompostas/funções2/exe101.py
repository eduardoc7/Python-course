def voto(dnascimento):
    from datetime import date # importação local dentro de uma função. Economizando memória!
    idade = date.today().year - dnascimento
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos. VOTO OPCIONAL!'
    elif idade < 16:
        return f'Com {idade} anos. NÃO VOTA!'
    else:
        return f'Com {idade} anos. VOTO OBRIGATÓRIO!'


nascimento = int(input('Em que ano vc nasceu amigão? '))
print(voto(nascimento))
 