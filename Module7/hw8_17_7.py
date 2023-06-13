import re
def token_parser(s):
    #regex = r"\d+[\*,\/,\-,\+,\(,\)]+\d+[\*,\/,\-,\+,\(,\)]"
    list_param_str =[]
    lexema=['*', '/', '-', '+', '(', ')']
    clean_s= s.replace(' ','')
    #print(clean_s)
    list_param_str1=re.findall('\d+',clean_s)
    list_param_str=s.split(list_param_str1)

    #match = clean_s.split(regex)
    #print(match)
    # for items in clean_s:

    #     if items in lexema:
    #         list_param_str= re.findall(items,clean_s)

    #     else:
    #         list_param_str1=re.findall('\d+',clean_s)
    #print(list_param_str)
    #print(list_param_str1)
    #for items in clean_s:
        
    #    print ()

        #list_param_str=clean_s.split(items)
    print(list_param_str)
    


    return list_param_str1
    
                
            
param_str= "2+ (34-5) * 3" # ['2', '+', '34', '-', '5', '*', '3']
print (token_parser(param_str))
    