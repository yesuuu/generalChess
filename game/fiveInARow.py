import numpy as np
from game import GameState


class FiveState(GameState):

    def __init__(self, boardSize=(10, 10)):
        self.board = np.zeros(boardSize)

    @staticmethod
    def _markWrapper(position, currentPlayer):
        def mark(board):
            board[position[0], position[1]] = currentPlayer
            return board
        return mark

    def getValidActions(self, currentPlayer):
        actions = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0:
                    actions.append(self._markWrapper((i, j), currentPlayer))

        return actions

    def act(self, action):
        self.board = action(self.board)

    def isEnd(self):
        return True if np.sum(self.board == 0) == 0 else False

    def showState(self):
        print '*' * (2 * self.board.shape[1] + 1)
        mapDict = {0:'-', 1:'o', 2:'x'}
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                print mapDict[self.board[i, j]],
            print
        print '*' * (2 * self.board.shape[1] + 1)

