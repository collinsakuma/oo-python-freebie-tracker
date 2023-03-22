import ipdb
from lib import *

#code here
apple = Company("Apple", 1976)
google = Company("Google", 1998)
ibm = Company('IBM', 1911)

collin = Dev("Collin")
saki = Dev("Saki")
jayson = Dev("Jason")

freebie1 = Freebie(collin, apple, "phone", 100)
freebie2 = Freebie(saki, google, "pen", 1)
freebie3 = Freebie(jayson, ibm, "engine", 101)

ipdb.set_trace()