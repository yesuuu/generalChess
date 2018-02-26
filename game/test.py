from twoHands import TwoHandState
from game import Game

s = TwoHandState()
# s.showState()
# actions = s.getValidActions(1)


g = Game(s, 1)
g.simulate(isShowState=True)
