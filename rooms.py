import definecards
from defineerrors import *
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
        self.rid=rid
        self.cards_not_used=[x for x in CARDS]
        self.players={}
    
    def allCards(self):
        return list(self.cards.keys())

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