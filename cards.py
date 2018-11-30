import definecards
import rooms
from definecards import CARDS, COLOURS, TYPES
from defineerrors import *

CARDS_USING = {}


class card(object): #Given card, in another word, card in use.
    def __init__(self, cid, cowner, croom):
        'croom accepts room object or croomid(str)'
        croom=rooms.getRoom(croom)
        croomid=croom.rid
        if cid in croom.cards:
            raise CardInUseError('Card cid: '+cid+' already in use.')
        else:
            croom.cards[cid]=self
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
            self.croom = croom
        except Exception as e:
            raise CardDefineError('Error while defining card cid: '+str(cid)+' :'+str(e))
        croom.cards_not_used.remove(cid)

    def destroy(self):
        'Destroy'
        self.croom.cards_not_used.append(self.cid)
        del(self.croom.cards[self.cid])
        del(self)

    def play(self):
        'User play this card.'
        self.croom.lastCard=self.cid
        self.destroy()


# 具体思路: 未发卡没有定义object,已出卡del(object),已发卡创建object并修改owner属性