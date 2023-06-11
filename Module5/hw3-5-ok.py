import re
from re import search

# phone = ["    +38(050)123-32-34", "     0503451234",
#        "(050)8889900", "38050-111-22-22", "38050 111 22 11   "]
phone = "    +38(050)123-32-34"


def sanitize_phone_number(phone):

    # print(phone)
    # for numbers in phone:
    new_phone = phone.strip()
    if new_phone.isalnum():
        return (new_phone)
    else:
        return (''.join((re.findall('(\d+)', new_phone))))
        # new_num.append(re.findall('(\d+)', new_phone))
    # return new_num


print(sanitize_phone_number(phone))
