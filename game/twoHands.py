from game import Game, GameState
import numpy as np


class TwoHandState(GameState):

    def __init__(self, initState=(1, 1, 1, 1), ):
        self.state = initState

    @staticmethod
    def addToPosition(positionChange, positionToAdd):
        def addTo(state):
            stateList = list(state)
            stateList[positionChange] += stateList[positionToAdd]
            return tuple(stateList)
        return addTo

    def getValidActions(self, currentPlayer):
        assert currentPlayer in (1, 2)
        actionList = []

        if currentPlayer == 1:
            if self.state[2] < 10:
                if self.state[0] < 10:
                    actionList.append(self.addToPosition(0, 2))
                if self.state[1] < 10:
                    actionList.append(self.addToPosition(1, 2))
            if self.state[3] < 10:
                if self.state[0] < 10:
                    actionList.append(self.addToPosition(0, 3))
                if self.state[1] < 10:
                    actionList.append(self.addToPosition(1, 3))

        if currentPlayer == 2:

            if self.state[2] < 10:
                if self.state[0] < 10:
                    actionList.append(self.addToPosition(2, 0))
                if self.state[1] < 10:
                    actionList.append(self.addToPosition(2, 1))
            if self.state[3] < 10:
                if self.state[0] < 10:
                    actionList.append(self.addToPosition(3, 0))
                if self.state[1] < 10:
                    actionList.append(self.addToPosition(3, 1))

        return actionList

    def act(self, action):
        self.state = action(self.state)

    def isEnd(self, currentPlayer):
        validActions = self.getValidActions(currentPlayer)
        if validActions:
            return False, None
        else:
            return True, 0 if currentPlayer == 1 else 1

    def getActionFromCmd(self, cmd):
        """
        cmd like '1,1,1'
        """
        nums = [int(x) for x in cmd.split(',')]
        player = nums[0]

        if player == 1 and nums[1] == 1:
            positionChange = 2
        elif player == 1 and nums[1] == 2:
            positionChange = 3
        elif player == 2 and nums[1] == 1:
            positionChange = 0
        elif player == 2 and nums[1] == 2:
            positionChange = 1
        else:
            raise Exception

        if player == 1 and nums[2] == 1:
            positionToAdd = 0
        elif player == 1 and nums[2] == 2:
            positionToAdd = 1
        elif player == 2 and nums[2] == 1:
            positionToAdd = 2
        elif player == 2 and nums[2] == 2:
            positionToAdd = 3
        else:
            raise Exception

        return self.addToPosition(positionChange, positionToAdd)

    def showState(self):
        print '*'*10
        print self.state[0], self.state[1]
        print self.state[2], self.state[3]
        print '*'*10

    def showActionWinRate(self, winRateDict):
        pass
