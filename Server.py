import cards
from cards import card, analyseCard, giveCard, randomCard
from rooms import room, findRoomById, getRoom
from players import player, findPlayerById, getPlayer
from random import randint
from defineerrors import *

SocketBand = ('', 9777)


def main():
    lounge = room('lounge')
    player_one = player('Lincoln')
    player_two = player('Sunny')
    player_three = player('David')
    player_one.join(lounge)
    player_two.join(lounge)
    player_three.join(lounge)
    randomCard(lounge, 'Lincoln', 3)
    randomCard(lounge, 'David', 3)
    randomCard(lounge, 'Sunny', 3)
    lounge.lastCard=lounge.cards_not_used[randint(-1, len(lounge.cards_not_used)-1)]
    while analyseCard(lounge.lastCard)[1]=='+2' or analyseCard(lounge.lastCard)[1]=='+4' or analyseCard(lounge.lastCard)[1]=='Reverse' or analyseCard(lounge.lastCard)[1]=='Skip':
        lounge.lastCard=lounge.cards_not_used[randint(-1, len(lounge.cards_not_used)-1)]
    lounge.currentColour = analyseCard(lounge.lastCard)[0]
    lounge.currentType = analyseCard(lounge.lastCard)[1]
    lounge.plusCount = 0
    import os
    try:
        while lounge:
            x = lounge.playTurn[lounge.currentPlayer]
            x = lounge.players[x]
            y=False
            p=False
            alreadyM=False
            unable=False
            Tip='Press . for more card.'
            chosen=[]
            while y == False:
                os.system('cls')
                print('Now', x.pid, 'is playing...')
                lasta=analyseCard(lounge.lastCard)
                print('Last card:',lounge.currentColour,lasta[3])
                print('You have', len(x.allCards()), 'cards:')
                for z in x.allCards():
                    print(z,x.cards[z].ccolour,x.cards[z].cdescription,end='',sep='\t')
                    if z in chosen:
                        print('\tCHOSEN:'+str(chosen.index(z)+1))
                    else:
                        print('')
                if Tip!='':
                    print('* '+Tip)
                    Tip='Press . for more card or press enter to submit.'
                if lounge.plusCount>0:
                    print('* Pending +'+str(lounge.plusCount)+'. Choose a +2 or +4 to avoid it.')
                i = input('>')
                if i == '':
                    if len(chosen)==0:
                        Tip='Please choose at least 1 card or press . for more card.'
                        unable=True
                    played=[]
                    for z in chosen:
                        y = x.play(z)
                        if y==False:
                            for l in played:
                                giveCard(lounge,x,l)
                            Tip='Unable to play those cards. Please try again.'
                            unable=True
                            chosen=[]
                            y=False
                            break
                        played.append(z)
                    if type(y)!=bool:
                        colour, ctype, number, description = analyseCard(y)
                        # print(colour, description,'was played.')
                if i == '.':
                    if alreadyM:
                        Syst=card('ZZZ',x,lounge)
                        cards.checkPlus(Syst)
                        Syst.destroy()
                        lounge.nextPlayer()
                        break
                    alreadyM=True
                    Tip='Press . if you still can not make a selection.'
                    randomCard(lounge, x, 1)
                    y = False
                    continue                
                if i in x.allCards():
                    if i in chosen:
                        chosen.remove(i)
                    else:
                        chosen.append(i)
                elif len(i)==2 and i in [ll[:2] for ll in x.allCards()]:
                    for ii in x.allCards():
                        if ii[:2]==i:
                            if ii in chosen:
                                chosen.remove(ii)
                            else:
                                chosen.append(ii)
                else:
                    if unable==False:
                        Tip='You do not own that card.'
                    unable=False
    except GameCompleted:
        print('Game Ended')


    # [TODO] Auto Generate


if __name__ == '__main__':
    main()
