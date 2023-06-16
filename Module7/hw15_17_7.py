data=[1, 2, [3, 4, [5, 6]], 7]
new_list=[]
def flatten(data):
    for elem in data:
        #print (elem)
        if elem is list():
            for item in elem:
                new_list.append(item)
            return new_list   
        else:
            new_list.append(elem)
            return new_list
        
                
   
    #return new_list

    
        
    
        
print(flatten(data))
        
        