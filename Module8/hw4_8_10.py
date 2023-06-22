import random
from random import randrange
min = 1 # 1
max = 49 # 5x36 # 6x49
quantity = 6

def get_numbers_ticket(min, max, quantity):
    if min>=1 and max<1000:
        set_dig=[]
        if quantity>=min and quantity<max: 
            set_dig=[]
            #set_list=[]
            num_list = [randrange(min, max) for i in range(max) ]
            #print(num_list)
            set_dig=random.sample(num_list, k=quantity)
            print(set_dig)
            return sorted(set_dig)
    return []
    
print(get_numbers_ticket(min, max, quantity))