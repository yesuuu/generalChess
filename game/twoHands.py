from game import Game, GameState
import numpy as np


class TwoHandState(GameState):

    def __init__(self, initState=(1, 1, 1, 1), ):
        self.state = initState
        self.actionWrapper = self._initActionWrapper()

    @staticmethod
    def _initActionWrapper():
        def addToPosition(positionChange, positionToAdd):
            def addTo(state):
                stateList = list(state)
                stateList[positionChange] += stateList[positionToAdd]
                return tuple(stateList)
            return addTo
        return addToPosition

    def getValidActions(self, currentPlayer):
        assert currentPlayer in (1, 2)
        actionList = []

        if currentPlayer == 1:
            if self.state[2] < 10:
                if self.state[0] < 10:
                    actionList.append(self.actionWrapper(0, 2))
                if self.state[1] < 10:
                    actionList.append(self.actionWrapper(1, 2))
            if self.state[3] < 10:
                if self.state[0] < 10:
                    actionList.append(self.actionWrapper(0, 3))
                if self.state[1] < 10:
                    actionList.append(self.actionWrapper(1, 3))

        if currentPlayer == 2:

            if self.state[2] < 10:
                if self.state[0] < 10:
                    actionList.append(self.actionWrapper(2, 0))
                if self.state[1] < 10:
                    actionList.append(self.actionWrapper(2, 1))
            if self.state[3] < 10:
                if self.state[0] < 10:
                    actionList.append(self.actionWrapper(3, 0))
                if self.state[1] < 10:
                    actionList.append(self.actionWrapper(3, 1))

        return actionList

    def act(self, action):
        self.state = action(self.state)

    def isEnd(self):
        return np.all(np.array(self.state) >= 10)

    def showState(self):
        print '*'*10
        print self.state[0], self.state[1]
        print self.state[2], self.state[3]
        print '*'*10

