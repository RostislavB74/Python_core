from functools import reduce
payment = [1, -3, 4]


def add(x, y):
    return x+y


def amount_payment(payment):

    result = reduce(add, payment, 0)
    return result


print(amount_payment(payment))
