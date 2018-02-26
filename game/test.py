from twoHands import TwoHandState
from fiveInARow import FiveState
from game import Game

# s = TwoHandState()
# # s.showState()
# actions = s.getValidActions(1)

s = FiveState((2, 4))

g = Game(s, 1)
g.simulate(isShowState=True)
