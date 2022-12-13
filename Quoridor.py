import pygame as pg

class Game:

    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.board[0][4] = 2
        self.board[8][4] = 1

game = Game()
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in game.board]))