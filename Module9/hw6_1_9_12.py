import re
def generator_numbers(string="'The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."):
    num_list=re.findall('\d+', string)
    i=0
    res=0
    
    while i < len(num_list):
        res+=sum_profit(num_list[i])
        i+=1
    yield res

def sum_profit(string):
    return int(string)

print(next(generator_numbers()))        
    