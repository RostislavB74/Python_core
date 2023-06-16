def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        #print(s[0])
        print(flatten(s[0]) + flatten(s[1:]))
        return(flatten(s[0]) + flatten(s[1:]))
    print(s[:1])
    return(s[:1] + flatten(s[1:]))
s = [1, 2, [3, 4, [5, 6]], 7]
print("Выпрямленный список: ", flatten(s))