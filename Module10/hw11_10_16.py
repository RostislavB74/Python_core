# from collections import UserString
string = '"fdd88fs456"'


# class NumberString(UserString):

def number_count(string):
    res = [len(list(filter(f, string)))
           for f in (str.isdigit(lambda x: not x.isalnum()))]
    # count =0
    # for i in string:
    #     if i.isdigit():
    #         count += 1
    print(res)
    return res


number_count(string)
# s = 'fddfs456!+'
# print(number_count.NumberString(string))

# print(*res, sep=' ')  # 5 3 2
