import cards
from cards import card
from rooms import room, findRoomById, getRoom
from players import player, findPlayerById, getPlayer
from random import randint

def giveCard(whichRoom,whichPlayer,whichCardID):
    return card(whichCardID,whichPlayer,whichRoom)

def randomCard(whichRoom,whichPlayer,howMuch):
    if len(whichRoom.cards_not_used)<howMuch:
        howMuch=len(whichRoom.cards_not_used)
        print('Not enough cards')
    reply=[]
    for x in range(howMuch):
        ran=randint(-1,len(whichRoom.cards_not_used)-1)
        reply.append(giveCard(whichRoom,whichPlayer,whichRoom.cards_not_used[ran]))
    return reply

def main():
    lounge=room('lounge')
    player_one=player('Lincoln')
    player_two=player('Sunny')
    player_three=player('David')
    player_one.join(lounge)
    player_two.join(lounge)
    player_three.join(lounge)
    randomCard(lounge,'Lincoln',10)
    randomCard(lounge,'David',10)
    played=player_three.play(player_three.allCards()[0])
    print('Played:',played)
    randomCard(lounge,'Sunny',10)
    print(player_one.allCards())
    print(player_two.allCards())
    print(player_three.allCards())
    #[TODO] Auto Generate
    lounge.lastCard
    lounge.currentColour
    lounge.plusCount

if __name__=='__main__':
    main()