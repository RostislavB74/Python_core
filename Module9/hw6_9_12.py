import re
def generator_numbers(string):
    str_list =string.split(' ')
    while i<= len(str_list):
        yield numbers.append(re.findall('\d+', elem[i]))
        i+=1
     
    
    
    
    def sum_profit(string):
        result =0
        for elem in numbers:
             result +=elem
        return result      
            
            
                
                
            
        
            
        
string="The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."


result =generator_numbers(string)
print(result)