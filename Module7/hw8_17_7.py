import re
def token_parser(s):
    if s:
        list_param_str =[]
        new_list=[]
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

        # for j in range(len(list_param_str)):
        #     if list_param_str[j] not in lexema:
        #         word+=list_param_str[j]
        #         new_list.append(word)
        #     else:    
        #         new_list.append(list_param_str[j])
            
        #print(new_list)

            
        #list_param_str1=re.findall('\d+',clean_s)
    
        
    
        return new_list
    else:
        return False
                
            
param_str= " 2+ (34-5) * 3 " # ['2', '+', '34', '-', '5', '*', '3']
print (token_parser(param_str))
    