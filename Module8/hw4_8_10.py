import random
from random import randrange
<<<<<<< HEAD
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
=======
min = 1  # 1
max = 100  # 5x36 # 6x49
quantity = 49


def get_numbers_ticket(min, max, quantity):

    set_dig = []
    set_list = []
    if (min >= 1) and (max < 1000):
        if (quantity >= min) and (quantity < max):
            set_num = {randrange(min, max) for i in range(max)}
            # print(set_num)
            set_list = list(set_num)
            set_dig = random.sample(set_list, k=quantity)
            # print(sorted(set_list))
            return sorted(set_dig)
    return


print(get_numbers_ticket(min, max, quantity))
>>>>>>> 39e7e6eb4731e30ba051a1b6dd28861eb357268c
