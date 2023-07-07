payment = [100, -3, 400, 23, 35, -100]


# def positive_values(list_payment):
#     list1 = []
#     for i in filter(lambda x: x > 0, payment):
#         list1.append(i)
#     return list1


def is_positive(num):
    return num >= 0


def positive_values(payment):
    list1 = filter(is_positive, payment)
    return list(list1)


print(positive_values(payment))
