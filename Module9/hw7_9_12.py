name = ["dan", "jane", "steve", "mike"]


def normal_name(list_name):
    new_list = []
    for i in map(lambda elem: new_list.append(elem.capitalize()), list_name):
        print(new_list)
    return (new_list)


print(normal_name(name))
