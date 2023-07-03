import re


def generator_numbers(string):
    numbers = re.findall('\d+', string)
    return numbers


string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."


def sum_profit(string):
    pass


print(generator_numbers(string))
