from .freebie import Freebie

class Company:
    
    all = []

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year
        Company.all.append(self)


    # could add @property so when calling can use company.freebies instead of company.freebies()
    # @property
    def freebies(self):
        # return [ f for f in Freebie.all if f.company == self]

        our_final_list = []
        for freebie in Freebie.all:
            if freebie.company == self:
                out_final_list.append(freebie)
        return our_final_list

    def dev(self):
        return [f.dev for f in self.freebies]

    def give_freebie(self, dev_instance, item_name, value):
        # freebie needs: def __init__(self, dev_instance, company_instance, item_name, value)
        
        Freebie(dev_instance, self, item_name, value)
    
    @classmethod
    def oldest_company(cls):
        # for company in Company.all:
        #could also use sort

        earliest_year = 3000
        found_instance = ''

        for company in cls.all:
            if company.founding_year < earliest_year:
                earliest_year = company.founding_year
                found_instance = company
        return found_instance
        # found_min = min( [c.founding_year for c in cls.all])
        # return [ c for c in cls.all if c.founding_year == found_min][0].name


