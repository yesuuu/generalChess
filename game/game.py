import random
import numpy as np


class Game(object):

    def __init__(self, gameState, currentPlayer):
        self.gameState = gameState
        assert currentPlayer in (1, 2)
        self.currentPlayer = currentPlayer

    def getValidActions(self):
        return self.gameState.getValidActions(self.currentPlayer)

    def changePlayer(self):
        self.currentPlayer = 1 if self.currentPlayer == 2 else 2

    def simulate(self, maxIter=np.inf, isShowState=True):
        print 'simulate start'
        iterNum = 0
        while not self.gameState.isEnd() and iterNum < maxIter:
            validAction = self.getValidActions()
            if not validAction:
                break
            action = random.choice(validAction)
            self.gameState.act(action)

            if isShowState:
                self.gameState.showState()
            self.changePlayer()
            iterNum += 1


class GameState(object):

    def __init__(self):
        pass

    def getValidActions(self, currentPlayer):
        pass

    def act(self, action):
        pass

    def isEnd(self):
        pass

    def showState(self):
        pass

