import re
def token_parser(s):
    if s:
        list_param_str =[]
        lexema=['*', '/', '-', '+', '(', ')']
        clean_s= s.replace(' ','')
        print(clean_s)
        for i in clean_s:
            if i in lexema:
                print(i)
            list_param_str.append(i)
        for j in range(len(list_param_str)):
            print(j)
            
        #list_param_str1=re.findall('\d+',clean_s)
    
        
    
        return list_param_str
    else:
        return False
                
            
param_str= " 2+ (34-5) * 3 " # ['2', '+', '34', '-', '5', '*', '3']
print (token_parser(param_str))
    