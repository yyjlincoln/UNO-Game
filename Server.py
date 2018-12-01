import cards
from cards import card, analyseCard, giveCard, randomCard
from rooms import room, findRoomById, getRoom
from players import player, findPlayerById, getPlayer
from random import randint

SocketBand=('',9777)



def main():
    lounge=room('lounge')
    player_one=player('Lincoln')
    player_two=player('Sunny')
    player_three=player('David')
    player_one.join(lounge)
    player_two.join(lounge)
    player_three.join(lounge)
    randomCard(lounge,'Lincoln',3)
    randomCard(lounge,'David',10)
    randomCard(lounge,'Sunny',10)
    lounge.lastCard = None
    lounge.currentColour = 'Blue'
    lounge.plusCount = 0
    try:
        while lounge:
            x=lounge.playTurn[lounge.currentPlayer]
            x=lounge.players[x]
            print('Now',x.pid,'is playing...')
            print('You have',len(x.allCards()),'cards:')
            print(x.allCards())
            i=input('>')
            if i=='i':
                randomCard(lounge,x,1)
                y=False
            else:
                y=x.play(i)
            while y==False:
                print('Retry:')
                print('You have',len(x.allCards()),'cards:')
                print(x.allCards())
                i=input('>')
                y=x.play(i)
                if i=='i':
                    randomCard(lounge,x,1)
                    y=False
                    continue
            colour,ctype,number,discription=analyseCard(y)
            print(colour,discription)
    except NameError:
        print('Game Ended')

    #[TODO] Auto Generate

if __name__=='__main__':
    main()