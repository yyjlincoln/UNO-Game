import rooms
from defineerrors import *

PLAYERS={}

class player(object):
    def __init__(self,pid,proom=None):
        if pid in PLAYERS:
            raise PlayerAlreadyExistError('This pid has already exists.')
        self.pid=pid
        if proom:
            proom=self.proom=rooms.getRoom(proom)
            proom.players[pid]=self
        else:
            self.proom=None
        self.cards={}
        PLAYERS[pid]=self
    
    def allCards(self):
        return list(self.cards.keys())
    
    def join(self,room):
        if self.proom!=None:
            self.quit()
        room=self.proom=rooms.getRoom(room)
        room.players[self.pid]=self
    
    def quit(self):
        try:
            del(self.proom.players[self.pid])
            for x in self.cards:
                x.destroy()
        except Exception as e:
            print(e)


def findPlayerById(playerid):
    if playerid not in PLAYERS:
        raise PlayerDoesnotExistError('Player id: '+playerid+' does not exist.')
    else:
        return PLAYERS[playerid]

def getPlayer(player):
    if type(player)==str:
        r=findPlayerById(player)
        try:
            t=r.pid
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