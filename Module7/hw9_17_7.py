data = [1, 2, 3]  # [[], [1],[2],[3],[1.2],[2,3],[1,2,3]]
new_list = [[]]
elem_list = []


def all_sub_lists(data):
    for elem in data:
        elem_list.append(elem)
    new_list.append(elem_list)

    for i in range(len(data)):

    return new_list


print(all_sub_lists(data))
