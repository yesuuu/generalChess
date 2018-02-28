import random
import numpy as np
from abc import abstractmethod


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
        while not self.gameState.isEnd()[0] and iterNum < maxIter:
            print 'itering ...'
            validActions = self.getValidActions()
            # print validAction
            action = random.choice(validActions)
            self.gameState.act(action)

            if isShowState:
                self.gameState.showState()
            self.changePlayer()
            iterNum += 1


class GameState(object):

    def __init__(self):
        pass

    @abstractmethod
    def getValidActions(self, currentPlayer):
        pass

    @abstractmethod
    def act(self, action):
        pass

    @abstractmethod
    def isEnd(self, currentPlayer):
        """return (False, None) or (True, Player1 win rate)"""
        pass

    @abstractmethod
    def getActionFromCmd(self, cmd):
        pass

    @abstractmethod
    def showState(self):
        pass

    @abstractmethod
    def showAction(self):
        pass

    @abstractmethod
    def showActionWinRate(self, winRateDict):
        pass


