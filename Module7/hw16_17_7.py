list_data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
str_data = "XXXZZXXYYYZZ"


def decode(data):
    counter = []
    doubles = []
    for elem in range(len(data)):
        counter.append(elem[0])

        counter[elem] = counter.get(elem, 0) + 1
        doubles = {elem: count for element,
                   count in counter.items() if count > 1}

    return doubles


data = list_data
print(decode(data))
data = str_data
print(decode(data))
