import cards
from cards import card
from rooms import room
from players import player

test=room('1')
play=player('1')
play.join('1')
a=card('R11','1',test)
b=card('R12',play,test)
print(a.ccolour,a.cdiscription)
print(play.allCards())
print(test.allCards())

def giveCard(whichRoom,whichPlayer,whichCardID):
   return card(whichCardID,whichPlayer,whichRoom)

def randomCard(whichRoom,whichPlayer):
    pass