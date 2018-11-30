import cards
from cards import card
from rooms import room

test=room('test')
a=card('R11','Lincoln',test)
print(test.cards)
a.play()
print(test.cards)
b=card('R11','Sunny','test')
print(test.cards)

def randomCard(whichRoom,whichPlayer):
    pass