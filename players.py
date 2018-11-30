import rooms
from defineerrors import *

PLAYERS={}

class player(object):
    def __init__(self,pid,proom):
        if pid in PLAYERS:
            raise PlayerAlreadyExistError('This pid has already exists.')
        self.pid=pid
        proom=self.proom=rooms.getRoom(proom)
        proom.players[pid]=self
        self.cards={}
    
    def allCards(self):
        return self.cards

def findPlayerById(playerid):
    if playerid not in PLAYERS:
        raise PlayerDoesnotExistError('Player id: '+playerid+' does not exist.')
    else:
        return PLAYERS[playerid]

def getPlayer(player):
    if type(player)==str:
        r=findPlayerById(player)
        try:
            t=r.rid
        except:
            raise PlayerDoesnotExistError('Invalid player: no pid.')
        return r
    elif isinstance(player,object):
        try:
            t=player.pid
        except:
            raise PlayerDoesnotExistError('Invalid player: no pid.')
        return player
    else:
        raise PlayerDoesnotExistError('This player does not exist.')