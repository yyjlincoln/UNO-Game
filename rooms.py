ROOMS={}

class room(object):
    def __init__(self,rid):
        global ROOMS
        ROOMS[rid]=self
        self.cards=[]
        self.lastCard=None