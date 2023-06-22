import random
from random import randrange
min = 1 # 1
max = 36 # 5x36 # 6x49
quantity = 36

def get_numbers_ticket(min, max, quantity):
    set_dig=[]
    set_num = {randrange(min, max) for i in range(quantity) }
    print(set_num)
    set_dig=random.sample(list(set_num), k=5)
    
    return set_dig
    
print(get_numbers_ticket(min, max, quantity))