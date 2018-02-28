from abc import abstractmethod

class Algo(object):

    def __init__(self, gameState, currentPlayer):
        self.gameState = gameState

    @abstractmethod
    def getWinRate(self, actions=None):
        pass

    @abstractmethod
    def choose(self):
        pass




class MinMax(Algo):

    def getNext(self, gameState):
        pass
