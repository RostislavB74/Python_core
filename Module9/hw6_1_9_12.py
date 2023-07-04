import re
string = "'The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."


def generator_numbers(string):
    i = 0
    num_list = re.findall("\d+", string)
    while i < len(num_list):
        # print(num_list[i])
        yield int(num_list[i])
        i += 1


def sum_profit(string):
    sum = 0
    for x in generator_numbers(string):
        # print(x)
        sum += x
    return sum


print(sum_profit(string))
