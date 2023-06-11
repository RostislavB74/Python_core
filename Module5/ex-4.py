lst_m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def flatten(data):
    result = []
    for element in data:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)

    return result


print(flatten(lst_m))
