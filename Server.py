import cards
from cards import card
from rooms import room

test=room('1')
a=card('R11','P1',test)
print(a.ccolour,a.cdiscription)

def randomCard(whichRoom,whichPlayer):
    pass