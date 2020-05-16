def fatorial(num, show=False):
    """
    => Calcula o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar a conta de um número.
    :return: Retorna o resultado do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f


# Main Program
print(fatorial(5, show=False))

