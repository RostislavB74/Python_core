data=[1, 2, [3, 4, [5, 6]], 7]
new_list=[]
def flatten(data):
    if data:
        for elem in data:
            print (elem)
            if elem is not list():
                new_list.append(elem)
                return new_list
            else:
                flatten(elem)
    else:
        return data
   
    #return new_list

    
        
    
        
print(flatten(data))
        
        