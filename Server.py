import cards
from cards import card, analyseCard
from rooms import room, findRoomById, getRoom
from players import player, findPlayerById, getPlayer
from random import randint

SocketBand=('',9777)

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
    randomCard(lounge,'Sunny',10)
    while 'lounge' in globals():
        for x in lounge.players:
            print('Now',x.pid,'is playing...')
            print('You have',len(x.cards),'cards:')
            print(x.cards)
            y=x.play(input('>'))
            while y==False:
                print('Invalid play, please retry!')
                y=x.play(input('>'))
            colour,ctype,number,discription=analyseCard(y)


    #[TODO] Auto Generate
    lounge.lastCard = None
    lounge.currentColour = 'Blue'
    lounge.plusCount = 0

if __name__=='__main__':
    main()