import re
from re import search


def is_check_name(fullname, first_name):

    res = re.search(first_name, fullname)
    return (bool(res))
    # def get_fullname(a='first_name', b='last_name', c=''):


   # if c:
    #    return a +' '+c+' '+b
    # else:
    #    return a+' '+ b
# print(get_fullname('R', 'B', 'C'))
fullname = "Alex Old"
first_name = "Alex"
print(is_check_name(fullname, first_name))
