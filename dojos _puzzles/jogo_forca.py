from random import choice


class Forca:
  tentativas = 3
  msg = 'Jogando!'

  palavras = [
    'carro', 'mercado', 
    'ovelha', 'computador', 
    'dados', 'teclado',
    'monitor', 'janela', 
    'arbusto', 'grama', 
    'copo', 'gato'
  ]

  def __init__(self):
    lista = self.__class__.palavras
    self.__class__.palavra = choice(lista)
  
  def menu(self):
    print('=:' * 30)
    print(f'{"Jogo da Forca!":^60}')
    print('=:' * 30)
    print(f'{"Voce ainda tem":^35}', end='')
    print(f'{self.__class__.tentativas} TENTATIVAS')
    print()
    print(f'{self.__class__.msg}')
    print()
    print('=:' * 30)

  def handle_word(self, letra, hide_word):
    palavra = self.__class__.palavra
    new_word = ''
    
    if letra == palavra:
      print('Parabéns você venceu!')
      self.__class__.tentativas = 0
    else:
      for k, w in enumerate(palavra):
        if letra == w:
          print()
          self.__class__.msg = 'Letra Certa!'
          hide_word[k] = letra
        else:
          print()
          self.__class__.msg = 'Letra Errada!'
      
      for w in hide_word:
        new_word += w

      print()
      print(new_word)

  def play(self):
    palavra = self.__class__.palavra
    hide_word = []

    for w in palavra:
      hide_word.append(w.replace(w, '_')) 
    
    while self.__class__.tentativas != 0:
      self.menu()
      letra = input('Digite uma letra: ')
      self.__class__.tentativas -= 1
      self.handle_word(letra, hide_word)
      

# Main Program      
test = Forca()
test.play()


     
