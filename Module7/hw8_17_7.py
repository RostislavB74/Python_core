import re
def token_parser(s):
    new_list=[]
    if s:
        list_param_str =[]
        
        word=''
        lexema=['*', '/', '-', '+', '(', ')']
        clean_s= s.replace(' ','')
        for j in range(len(clean_s)):
            
            if clean_s[j] not in lexema:
                word += clean_s[j]
                #count = word
                continue
            else:
                if word!='':
                    new_list.append(word)
                    new_list.append(clean_s[j])
                    word=''
                else:
                    new_list.append(clean_s[j])
                    word=''
        #     for i in clean_s:
            
        #     if i not in lexema:
        #         word +=i
        #         continue
        #     new_list.append(i)

        new_list.append(word)
    
        return new_list
    else:
        return new_list
                
            
param_str= " 2+ 34-5 * 3 " # ['2', '+', '34', '-', '5', '*', '3']
print (token_parser(param_str))
    