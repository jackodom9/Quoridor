import pygame as pg

class Game:

    def __init__(self):
        # initialize board as array of zeroes, where
        # zeroes signify empty square

        self.board = [[0 for i in range(9)] for j in range(9)]

        # initialize player 2 position
        self.board[0][4] = 2

        # initialize player 1 position
        self.board[8][4] = 1

        # initialize player walls
        wallsPlayer1 = 10
        wallsPlayer2 = 10

        # initialize player1 Turn
        player1Turn = True

        # initialize walls array
        # zeroes are empty 3, is vertical, 4 is horizontal
        walls = [[0 for i in range(8)] for j in range(8)]
    
    # params i, j: indices of desired move
    def attemptMove(self, moveLocation, player):
        # find player location
        playerLocation = self.findPlayer(self, player)
        if player == 1:
            enemyLocation = self.findplayer(self, 2)
        else:
            enemyLocation = self.findplayer(self, 1)
        # check if valid move
        isValid = self.isValidMove(self, moveLocation, playerLocation, player)
        # check if jump
        # make move
        return True

    # helper method to find player location in board
    def findPlayer(self, player):
        playerLocation = [0,0]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == player:
                    playerLocation[0] = i
                    playerLocation[1] = j
        return playerLocation

    # helper method to determine if move is valid
    def isValidMove(self, moveLocation, playerLocation, player):
        return self.isCloseEnough(self, moveLocation, playerLocation) and self.isWallBlocking(self, moveLocation, playerLocation)

    # helper method for isValidMove
    def isCloseEnough(self, moveLocation, playerLocation):
        # close enough flag
        closeFlag = False
        # determine if close enough
        validMoves = []
        validMoves.append([playerLocation[0] + 1, playerLocation[1]])
        validMoves.append([playerLocation[0] - 1, playerLocation[1]])
        validMoves.append([playerLocation[0], playerLocation[1] + 1])
        validMoves.append([playerLocation[0], playerLocation - 1])
        for move in validMoves:
            if moveLocation == move:
                closeFlag = True
        return closeFlag
    
    # helper method for isValidMove
    def isWallBlocking(self, moveLocation, playerLocation):
        if playerLocation[0] == moveLocation[0]:
            
        else:



        

game = Game()
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in game.board]))