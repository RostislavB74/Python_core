
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]


def add(x, y):
    return x+y


def sum_numbers(numbers):
    result = reduce(add, numbers, 0)
    return result


print(sum_numbers(numbers))
