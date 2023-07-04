import re
def generator_numbers(string="'The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."):
    i=0
    res=0
    num_list=re.findall('\d+', string)
    print(num_list)
    while i < len(num_list):
        print(num_list[i])
        q=num_list[i]
        
        i+=1
    yield sum_profit(q)  
    def sum_profit(q):
        #print(q)
        res+=int(q)
        return res
    

print(next(generator_numbers()))
    