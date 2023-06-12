def data_preparation(list_data):
    new_list = []
    new = []
    for elem in list_data:
        if len(elem) > 2:
            elem = sorted(elem)
            elem.pop(0)
            elem.pop(-1)
        #    print(elem)
        # print(elem)
        new_list.extend(elem)
    new_list.sort(key=None, reverse=True)
    # print(new_list)

    return new_list


list_data = [[1, 2, 3], [3, 4], [5, 6]]
print(data_preparation(list_data))
