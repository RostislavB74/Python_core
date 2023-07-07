from functools import reduce
payment = [1, -3, 4]


def add(x, y):
    return x+y


def amount_payment(payment):
    list_b = [x for x in payment if x > 0]
    # print(list_b)
    result = reduce(add, list_b, 0)
    return result


print(amount_payment(payment))
