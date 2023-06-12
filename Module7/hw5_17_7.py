def capital_text(s):
<<<<<<< HEAD
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
=======
    new_list=[]
    symbol_list=['.','!','?']
    if len(s)==0:
        return False
    if len(s)==1:
        new_str = s.capitalize()
        return new_str
    if len(s)>=1:
        new_list = s.split(' ')
        #print(new_list)
        for items in new_list:
            #print(items)
            #items[0]= items[0].capitalize()
            for letter in items:
                print(letter[-1])
                #if letter[-1] in symbol_list:
                #    items = items.capitalize()
            #print()    
        #new_str=s.strip()
        #if new_str[0] in symbol_list:
        #    new_str=new_str.removeprefix(new_str[0])
        #    new_str=new_str.lstrip()
        #    new_str=new_str.capitalize()
        return s
       
        # if d[0] in symbol_list:
        #     d = d.removeprefix(d[0])
        #         #str_new = ''.join(new_d)
        #         #try:
        # if d.isdigit():
        #     return True
        # else:
        #     return False
        
    #print(d)

    #dig = re.search('+', s)
    #print(dig)

    #if len(s) == 0:
    #    return False
    #if dig:
    #    return True


s = 'alert. boss! oh' #'Alert. Boss! Oh'
>>>>>>> 0a4f2f4892deea49f19fa5aa1a7bcc09ad86a62c

print(capital_text(s))
