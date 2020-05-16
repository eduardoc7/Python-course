def notas(*args, sit=False):
    """
    => Função para analisar as notas e situação de vários alunos
    :param args: Uma ou mais notas dos alunos (aceita várias).
    :param sit: (opcional), indica a situação dos alunos.
    :return: Retorna um dicionário com todas as informações.
    """
    datas = dict()
    datas['total'] = len(args)
    datas['maior'] = max(args)
    datas['menor'] = min(args)
    media = 0
    for valor in args:
        media += valor
    datas['media'] = media / len(args)
    if sit:
        if datas['media'] >= 7:
            datas['situação'] = 'BOA!'
        elif media >= 5:
            datas['situação'] = 'RAZOÁVEL!'
        else:
            datas['situação'] = 'RUIM'
    return datas


# Main Program
resp = notas(7, 7, 7, sit=False)
print(resp)
