import definecards
from definecards import CARDS, COLOURS, TYPES
from room import ROOMS

CARDS_USING = {}

class RoomDoesnotExistError(Exception):
    # Room does not exist
    pass

class CardDefineError(Exception):
    # CardDefinerror
    pass


class CardInUseError(Exception):
    # This card is already in use.
    pass

class card(object): #Given card, in another word, card in use.
    def __init__(self, cid, cowner, croomid):
        if croomid not in ROOMS:
            raise RoomDoesnotExistError('Room id: '+croomid+' does not exist.')
        if cid in ROOMS[croomid].cards:
            raise CardInUseError('Card cid: '+cid+' already in use.')
        else:
            ROOMS[croomid].cards[cid]=self
        self.cid = cid
        cidsplit = list(cid)
        if len(cidsplit) != 3:
            raise CardDefineError('Can not define card: len(cidsplit) should equal to 3. Got '+str(len(cidsplit))+'.')
        if cidsplit[0] not in COLOURS:
            raise CardDefineError('Can not map colour for cid: '+cid)
        self.ccolour = COLOURS[cidsplit[0]]
        if cidsplit[1] not in TYPES:
            raise CardDefineError('Can not map type for cid: '+cid)
        self.ctype = TYPES[cidsplit[1]]
        if cid not in CARDS:
            raise CardDefineError('Card cid: '+cid+' does not exist.')
        try:
            self.cnumber = int(cidsplit[2])
            self.cdiscription = CARDS[cid]
            self.cowner = cowner
            self.croomid = croomid
        except Exception as e:
            raise CardDefineError('Error while defining card cid: '+str(cid)+' :'+str(e))

    def destroy(self):
        'Destroy'
        del(ROOMS[self.croomid].cards[self.cid])
        del(self)

    def play(self):
        'User play this card.'
        ROOMS.lastCard=self.cid
        self.destroy()


# 具体思路: 未发卡没有定义object,已出卡del(object),已发卡创建object并修改owner属性