def is_integer(s):
    new_d=[]
    symbol_list=['+','-']
    if len(s)==0:
        return False
    if len(s)>=1:
        print(s)
        d=s.strip()
        if len(d)==0:
            return False
        if len(d)==1:
            if d.isdigit():
                return True
            print(d)
        if d[0] in symbol_list:
            d = d.removeprefix(d[0])
                #str_new = ''.join(new_d)
                #try:
        if d.isdigit():
            return True
        else:
            return False
        
    #print(d)

    #dig = re.search('+', s)
    #print(dig)

    #if len(s) == 0:
    #    return False
    #if dig:
    #    return True


s = '  '

print(is_integer(s))

# def is_integer(s):
#     new_d=''
#     symbol_list=['+','-']
#     if len(s)>=1:
#         d=s.strip()
        
#         if d[0] in symbol_list:
#             #print(d[0])
#             new_d = d.removeprefix(d[0])
#             print(new_d)
#             if new_d.isdigit():
#                 return True
#         # try:
#         #    if new_d.isdigit():
#         #        return True
#         # except ValueError:
#             else:
#                 return False
            
#     else:
#          return False
# s = ' -+2 '
# print(is_integer(s))