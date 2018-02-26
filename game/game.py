
class Game(object):

    def __init__(self, gameState, currentPlayer):
        self.gameState = gameState
        assert currentPlayer in (1, 2)
        self.currentPlayer = currentPlayer

    def getValidActions(self):
        self.gameState.getValidActions(self.currentPlayer)

    def act(self, action, ):
        self.gameState.act(action, self.currentPlayer)
        self.changePlayer()

    def changePlayer(self):
        self.currentPlayer = 1 if self.currentPlayer == 2 else 2

    def simulate(self):
        pass


class GameState(object):

    def __init__(self):
        pass

    def getValidActions(self, currentPlayer):
        pass

    def act(self, action, currentPlayer):
        pass

    def isEnd(self):
        pass

    def showState(self):
        pass

