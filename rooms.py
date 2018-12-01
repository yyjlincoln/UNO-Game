import definecards
from defineerrors import *
import players
CARDS=definecards.CARDS.copy()

ROOMS={}

class room(object):
    def __init__(self,rid):
        global ROOMS
        if rid in ROOMS:
            raise RoomAlreadyExistError('This rid has already exists.')
        ROOMS[rid]=self
        self.cards={}
        self.lastCard=None
        self.currentColour=None
        self.plusCount=0
        self.rid=rid
        self.cards_not_used=[x for x in CARDS]
        self.players={}
        self.winners={}
        self.currentPlayer=0
        self.skipCount=0
        self.currentType=None
        self.orientation=True #Clockwise
        self.playTurn=[]
    
    def allCards(self):
        return list(self.cards.keys())
    
    def winner(self,pid):
        self.winners[pid]=players.findPlayerById(pid)
        print(pid,'is the %s Winner!'%str(len(self.winners)))
        if len(self.players)==len(self.winners):
            print('Game ends!')
            self.destroy()
    
    def destroy(self):
        for x in self.players:
            self.players[x].quit()
        for x in self.cards:
            self.cards[x].destroy()

    def nextPlayer(self):
        if self.orientation == True:  # Next Player
            if self.currentPlayer == len(self.playTurn)-1:
                self.currentPlayer = 0
            else:
                self.currentPlayer += 1
        else:
            if self.currentPlayer == 0:
                self.currentPlayer = len(self.playTurn)-1
            else:
                self.currentPlayer -= 1


def findRoomById(roomid):
    if roomid not in ROOMS:
        raise RoomDoesnotExistError('Room id: '+roomid+' does not exist.')
    else:
        return ROOMS[roomid]
    
def getRoom(room):
    if type(room)==str:
        r=findRoomById(room)
        try:
            t=r.rid
        except:
            raise RoomDoesnotExistError('Invalid room: no rid.')
        return r
    elif isinstance(room,object):
        try:
            t=room.rid
        except:
            raise RoomDoesnotExistError('Invalid room: no rid.')
        return room
    else:
        raise RoomDoesnotExistError('This room does not exist.')
