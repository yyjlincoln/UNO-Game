import definecards
import rooms
import players
from definecards import CARDS, COLOURS, TYPES
from defineerrors import *
import random

plusCardTrigger=None #plusCardTrigger(number of cards, [cards in object form])
CARDS_USING = {}


class card(object):  # Given card, in another word, card in use.
    def __init__(self, cid, cowner, croom):
        'croom accepts room object or croomid(str)'
        croom = rooms.getRoom(croom)
        cowner = players.getPlayer(cowner)
        croomid = croom.rid
        if cid in croom.cards:
            raise CardInUseError('Card cid: '+cid+' already in use.')
        else:
            croom.cards[cid] = self
            cowner.cards[cid] = self
        if cowner.proom == None or cowner.proom.rid != croom.rid:
            if cowner.proom == None:
                raise PlayerNotInRoomError(
                    'Player pid '+cowner.pid+' is not in any rome but the current room is rid '+croom.rid)
            else:
                raise PlayerNotInRoomError(
                    'Player pid '+cowner.pid+' is in room rid '+cowner.proom.rid+' but the current room is rid '+croom.rid)
        self.cid = cid
        self.ccolour, self.ctype, self.cnumber, self.cdescription = analyseCard(
            cid)
        self.cowner = cowner
        self.cownerid = cowner.pid
        self.croomid = croomid
        self.croom = croom
        croom.cards_not_used.remove(cid)

    def destroy(self):
        'Destroy'
        self.croom.cards_not_used.append(self.cid)
        try:
            del(self.croom.cards[self.cid])
            del(self.cowner.cards[self.cid])
            del(self)
        except:
            pass

    def play(self):
        'User play this card.'
        # Play card
        if not playable(self):
            raise InvalidStep('Not playable')
        self.croom.lastCard = self.cid
        self.croom.currentColour = self.ccolour
        self.croom.currentType = self.ctype
        typeCheck(self)
        checkPlus(self)
        if len(self.cowner.cards) == 1:
            self.cowner.quit()
            self.croom.winner(self.cownerid)
        # Play end
        # playerSelected(self)
        self.destroy()


def analyseCard(cid):
    cidsplit = list(cid)
    if len(cidsplit) != 3:
        raise CardDefineError(
            'Can not define card: len(cidsplit) should equal to 3. Got '+str(len(cidsplit))+'.')
    if cidsplit[0] not in COLOURS:
        raise CardDefineError('Can not map colour for cid: '+cid)
    ccolour = COLOURS[cidsplit[0]]
    if cidsplit[1] not in TYPES:
        raise CardDefineError('Can not map type for cid: '+cid)
    ctype = TYPES[cidsplit[1]]
    if cid not in CARDS:
        raise CardDefineError('Card cid: '+cid+' does not exist.')
    cnumber = cidsplit[2]
    cdescription = CARDS[cid]
    return ccolour, ctype, cnumber, cdescription


def playable(ccard):
    currentRoom = ccard.croom
    if ccard.ccolour == 'Any':
        return True
    # if currentRoom.plusCount>0 and ccard.ctype!='+2' and ccard.ctype!='+4':
    #     # PlusCount
    #     return False
    if currentRoom.skipCount > 0:
        return False
    # if currentRoom.players[currentRoom.playTurn[currentRoom.currentPlayer]]!=ccard.cowner:

    #     return False
    if currentRoom.currentColour == ccard.ccolour:
        return True
    if currentRoom.currentType == ccard.ctype:
        return True
    return False

def testPlayable(baseColour,baseType,cardList):
    if len(cardList)>=1:
        if cardList[0].ccolour=='Any':
            anyAllowed=True
        else:
            anyAllowed=False
        res=[]
        for x in cardList:
            r ,baseColour, baseType = testPlay(baseColour, baseType, x, anyAllowed=anyAllowed)
            res.append(r)
        return all(res)

def testPlay(baseColour, baseType, singleCard, anyAllowed=False):
    if singleCard.ccolour==baseColour:
        return True, baseColour
    




def typeCheck(ccard):
    if ccard.ctype == '+2':
        ccard.croom.plusCount += 2
    elif ccard.ctype == '+4':
        ccard.croom.plusCount += 4
        pickColour(ccard.croom)
    elif ccard.ctype == 'Colour':
        pickColour(ccard.croom)
    elif ccard.ctype == 'Reverse':
        # print('REVERSE')
        if ccard.croom.orientation == False:
            ccard.croom.orientation = True
        else:
            ccard.croom.orientation = False
        # print(ccard.croom.orientation)
    elif ccard.ctype == 'Skip':
        ccard.croom.skipCount += 1


def playerSelected(ccard):
#    print('Next player selected.')
    ccard.croom.skipCount = 0
    pass


def checkPlus(ccard):
    if ccard.croom.plusCount > 0 and ccard.ctype != '+4' and ccard.ctype != '+2':
        applyPlus(ccard.croom,ccard.cowner)
    # Else no add

def applyPlus(croom,cwho):
    r=randomCard(croom, cwho, croom.plusCount)
    croom.plusCount = 0
    if plusCardTrigger:
        plusCardTrigger(croom.plusCount,r)

def pickColour(room):
    print('''B\tBlue
Y\tYellow
G\tGreen
R\tRed''')
    colourinput = input('Input Colour:')
    a = colourinput in COLOURS
    while a==False:
        colourinput = input('Input Colour:')
        a = colourinput in COLOURS
    room.currentColour=COLOURS[colourinput]


def giveCard(whichRoom, whichPlayer, whichCardID):
    return card(whichCardID, whichPlayer, whichRoom)


def randomCard(whichRoom, whichPlayer, howMuch):
    if len(whichRoom.cards_not_used) < howMuch:
        howMuch = len(whichRoom.cards_not_used)
        print('Not enough cards')
    reply = []
    for x in range(howMuch):
        ran = random.randint(-1, len(whichRoom.cards_not_used)-1)
        reply.append(giveCard(whichRoom, whichPlayer,
                              whichRoom.cards_not_used[ran]))
    return reply

# 具体思路: 未发卡没有定义object,已出卡del(object),已发卡创建object并修改owner属性
