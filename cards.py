import definecards
import rooms
from definecards import CARDS, COLOURS, TYPES
from defineerrors import *

CARDS_USING = {}


class card(object):  # Given card, in another word, card in use.
    def __init__(self, cid, cowner, croom):
        'croom accepts room object or croomid(str)'
        croom = rooms.getRoom(croom)
        croomid = croom.rid
        if cid in croom.cards:
            raise CardInUseError('Card cid: '+cid+' already in use.')
        else:
            croom.cards[cid] = self
        self.cid = cid
        self.ccolour, self.ctype, self.cnumber, self.cdiscription = analyseCard(cid)
        self.cowner = cowner
        self.croomid = croomid
        self.croom = croom
        croom.cards_not_used.remove(cid)

    def destroy(self):
        'Destroy'
        self.croom.cards_not_used.append(self.cid)
        del(self.croom.cards[self.cid])
        del(self)

    def play(self):
        'User play this card.'
        self.croom.lastCard = self.cid
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
    cnumber = int(cidsplit[2])
    cdiscription = CARDS[cid]
    return ccolour, ctype, cnumber, cdiscription

# 具体思路: 未发卡没有定义object,已出卡del(object),已发卡创建object并修改owner属性