from .freebie import Freebie

class Dev:

    def __init__(self, name):
        self.name = name

    def freebies(self):
        #return [ f for f in Freebie.all if f.dev == self]

        dev_freebie_list = []
        for freebie in Freebie.all:
            if freebie.dev == self:
                dev_freebie_list.append(freebie)
        return dev_freebie_list

    def companies(self):
        return [ f.company for f in self.freebies]

    def recieved_one(self, item_name):
        the_list = [ f.item_name for f in self.freebies if f.item_name == item_name]
        if len(the_list) > 0:
            return True
        else:
            return False
        
    #adamn.received_one('sticker')

    # for freebie in Freebie.all:
    #     if freebie.dev == self and freebie.item_name == item_name:
    #         return True
    #     else:
    #         return False


        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False

    def give_away(self):
        if freebie.dev == self:
            freebie.dev = dev
        else: print("Not yours to give away!")