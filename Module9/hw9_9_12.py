payment = [100, -3, 400, 23, 35, -100]


def positive_values(list_payment):
    list1 = []
    for i in filter(lambda x: x > 0, payment):
        list1.append(i)
    return list1


print(positive_values(payment))
