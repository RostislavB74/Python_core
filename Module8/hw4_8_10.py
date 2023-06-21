import random
from random import randrange
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
