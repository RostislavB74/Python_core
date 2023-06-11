def is_integer(s):
    import re
    # print(type(s))
    dig = re.findall('\d+', s)
    print(dig)

    if len(s) == 0:
        return False
    if dig:
        return True


s = ' +- 5  '

print(is_integer(s))
