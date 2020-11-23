class Game:
  __board = []
  __positions = {}
  __player = ''
  __sboard = ''
  __playing = False
  __plays = 0

  def __init__(self, board, positions, player, playing, plays, sboard):
    self.__board = board
    self.__positions = positions
    self.__player = player
    self.__playing = playing
    self.__plays = plays
    self.__sboard = sboard
  
  def play(self):
    move = 0
    self.show_board(self.__board, self.__sboard)

    move = int(input(f'Type the position to play 1-9 - Player >{self.__player}< : ' ))

    self.validate_move(move)

  def show_board(self, board, sboard):
    print(sboard)
    for l in range(0, 3):
      print('---+---+---' if l != 0 else '')
      for c in range(0, 3):
        print(f'{board[l][c]:^3}' if c == 2 else f'{board[l][c]:^3}|', end='')
      print()
  
  def validate_move(self, move):
    while True:
      try:
        if not 1 <= move <= 9:
          print('Invalid Position!')
          self.play()

        if self.__board[self.__positions[move][0]][self.__positions[move][1]] != '':
          print('Busy Position!')
          self.play()
          
        self.__board[self.__positions[move][0]][self.__positions[move][1]] = self.__player
      except (KeyError):
          print('Try a valid position!')
      else:
        if self.__player == 'O':
          self.__player = 'X'
        else:
          self.__player = 'O'
        self.play()
  


