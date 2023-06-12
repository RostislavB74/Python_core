def capital_text(s):
    r = ''
    symbol_list = ['.', '!', '?']
    if len(s) == 0:
        return False
    if len(s) == 1:
        new_str = s.capitalize()
        return new_str
    if len(s) >= 1:

        s = s.capitalize()
        i = 0
        while i < len(s):
            if s[i] in symbol_list:
                r = r + s[i]+s[i+1]+s[i+2].title()
                i += 3
                continue
            r += s[i]
            i += 1
        print(r)

    return r

    # if d[0] in symbol_list:
    #     d = d.removeprefix(d[0])
    #         #str_new = ''.join(new_d)
    #         #try:
    # if d.isdigit():
    #     return True
    # else:
    #     return False

    # print(d)

    # dig = re.search('+', s)
    # print(dig)

    # if len(s) == 0:
    #    return False
    # if dig:
    #    return True


s = 'alert. boss! oh'  # 'Alert. Boss! Oh'
capital_text(s)
