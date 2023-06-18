list_data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
str_data = "XXXZZXXYYYZZ"

new_list = []


def decode(data):
    if data == []:
        return data
    new_list.append(data[0])
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            new_list.append(count)
            new_list.append(data[i])
            count = 1
    new_list.append(count)
    return new_list


data = list_data
print(decode(data))
