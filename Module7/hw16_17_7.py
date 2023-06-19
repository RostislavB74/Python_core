list_data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
str_data = "XXXZZXXYYYZZ"

def decode(data):
    new_list = []
    print (data)
    if len(data) >0:
        list_1 = list(data[0])* data[1]
        list_2 = decode (data[2:])
        new_list = list_1+ list(list_2)
    return new_list
data = str_data
print(decode(data))
