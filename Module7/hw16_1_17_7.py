list_data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
str_data = "XXXZZXXYYYZZ"

def decode(data):
    new_list = []
    if len(data)<0:
        decode(data)
    if len(data)>0:
        new_list = []
        print (data)
    for n in range (0, len(data), 2):
        new_list.extend(data[n]*data[n+1])
    return new_list
    #     list_1 = list(data[0])* data[1]
    #     list_2 = decode (data[2:])
    #     new_list = list_1+ list(list_2)
    # return new_list
data = list_data
print(decode(data))
