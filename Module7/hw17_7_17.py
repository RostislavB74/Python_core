#list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2 ]
list=['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']

def encode(data):
    if not data:
        return []
    count =1
    current = data[0]
    while count < len(data) and data[count]==current:
        count+=1    
    return [data[0], count]+ encode(data[count:])

    # new_list = []
    # list_1=[]
    #     #print (data)
    # if len(data) >0:
    #     for i in range (data[1]):
    #         #print(i)
    #         new_list.append(data[0])
    #         #print(new_list)
    #         list_2 = encode (data[2:])
    #         #print(list_2)
    #     new_list.extend(list_2)
    # return new_list
        
print(encode(list))
    
    