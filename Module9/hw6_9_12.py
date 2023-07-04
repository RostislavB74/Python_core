import re
def generator_numbers(string):
    str_list = string.split(' ')
    # for i in len(str_list)
    print(str_list)
    numbers = []
    result = 0

    for elem in str_list:
        if elem.isalpha():
            continue
        #yield # print(elem)
        if re.findall('\d+', elem):
            res_1 = re.findall('\d+', elem)
            result += int(sum_profit(res_1))
    return result
def sum_profit(res_1):
    print(res_1)
    res = int(res_1[0])
    return res

#string = "The resulting profit was: from the southern pos200sessions 100$ 100, from the northern colonies $500, and the king gave $1000."
string="The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."

result = generator_numbers(string)
print(result)

# import re
# def generator_numbers(string):
#     str_list = string.split(' ')
#     print(str_list)
#     # for i in len(str_list)
#     numbers = []
#     result = 0
#     i=0
#     while i<= len(str_list):
#         print (i)
#         if re.findall('\d+', elem):
#             res_1 = re.findall('\d+', elem)
#             result += int(sum_profit(res_1))
#             yield elem
#         i+=1
#     return result
# def sum_profit(res_1):
#     print(res_1)
#     res = int(res_1[0])
#     return res

# #string = "The resulting profit was: from the southern pos200sessions 100$ 100, from the northern colonies $500, and the king gave $1000."
# string="The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."

# result = generator_numbers(string)
# print(result)
