import ipdb
from lib import *

#code here

apple = Company('Apple', 1976)
ibm = Company('IBM', 1911)
google = Company('Google', 1998)

adam = Dev('Adam')
emily = Dev('Emily')

#class Freebie
#def __init__(self, dev_instance, company_instance, item_name, value):

f1 = Freebie(adam, apple, "sticker", 5)
f1 = Freebie(emily, google, "lambo", 250000)

ibm.give_freebie(emily, "Rolex", 70000)

ipdb.set_trace()