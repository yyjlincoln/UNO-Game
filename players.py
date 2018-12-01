import rooms
from defineerrors import *

PLAYERS = {}


class player(object):
    def __init__(self, pid, proom=None):
        if pid in PLAYERS:
            raise PlayerAlreadyExistError('This pid has already exists.')
        self.pid = pid
        if proom:
            proom = self.proom = rooms.getRoom(proom)
            proom.players[pid] = self
        else:
            self.proom = None
        self.cards = {}
        PLAYERS[pid] = self

    def allCards(self):
        return list(self.cards.keys())

    def join(self, room):
        if self.proom != None:
            self.quit()
        room = self.proom = rooms.getRoom(room)
        room.players[self.pid] = self
        room.playTurn = list(room.players.keys())

    def quit(self):
        # if self.proom.currentPlayer > len(self.proom.playTurn)-1:
        #     self.proom.currentPlayer = len(self.proom.playTurn)-1
        self.proom.playTurn.remove(self.pid)
        del(self.proom.players[self.pid])
        s = self.cards.copy()
        for x in s:
            s[x].destroy()
        del(s)
        self.proom.nextPlayer()

    def play(self, cid):
        if cid in self.cards:
            # if self.proom.currentColour=='Any' or self.proom.currentColour==self.cards[cid].ccolour or self.proom.currentType==self.cards[cid].ctype:
            try:
                self.cards[cid].play()
            except InvalidStep:
                return False
            return cid
            # print(self.proom.currentColour,self.cards[cid].ccolour)

        return False


def findPlayerById(playerid):
    if playerid not in PLAYERS:
        raise PlayerDoesnotExistError(
            'Player id: '+playerid+' does not exist.')
    else:
        return PLAYERS[playerid]


def getPlayer(player):
    if type(player) == str:
        r = findPlayerById(player)
        try:
            t = r.pid
        except:
            raise PlayerDoesnotExistError('Invalid player: no pid.')
        return r
    elif isinstance(player, object):
        try:
            t = player.pid
        except:
            raise PlayerDoesnotExistError('Invalid player: no pid.')
        return player
    else:
        raise PlayerDoesnotExistError('This player does not exist.')
