from Game import Game

board = [['', '', ''], ['', '', ''], ['', '', '']]
positions = {
   1 : [0, 0],
   2 : [0, 1],
   3 : [0, 2],
   4 : [1, 0],
   5 : [1, 1],
   6 : [1, 2],
   7 : [2, 0],
   8 : [2, 1],
   9 : [2, 2],
}

player = 'X'
playing = True
plays = 0

sboard = """
positions
1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
7 | 8 | 9
"""

a = Game(board, positions, player, playing, plays, sboard)
a.play()





