class Freebie:
    
    all = []

    def __init__(self, dev_instance, company_instance, item_name, value):
        self.dev = dev_instance
        self.company = company_instance
        self.item_name = item_name
        self.value = value
        Freebie.all.append(self)
