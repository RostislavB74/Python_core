list = ["X", 3, "Z", 2]


def encode(data):
    new_list = []
    list_1=[]
        #print (data)
    if len(data) >0:
        for i in range (data[1]):
            #print(i)
            new_list.append(data[0])
            #print(new_list)
            list_2 = encode (data[2:])
            #print(list_2)
        new_list.extend(list_2)
    return new_list
        
print(encode(list))
    
    