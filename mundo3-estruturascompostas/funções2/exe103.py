def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {goals} gol(s) no campeonato.')


# Main Program
nome = str(input('Nome do jogador: '))
goals = str(input('Número de Goals: '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if nome.strip() == '':
    ficha(g=goals)
else:
    ficha(nome, goals)
