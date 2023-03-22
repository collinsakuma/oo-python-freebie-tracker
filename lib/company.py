from .freebie import Freebie

class Company:
    def __init__(self, name, founded_year):
        self.name = name
        self.founded_year = founded_year

    def freebies(self):
        freebies_list = []
        for freebie in Freebie.all:
            if freebie.company == self:
                freebies_list.append(freebie)
        return freebies_list
