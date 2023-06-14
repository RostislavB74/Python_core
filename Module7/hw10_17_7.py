keys=['name', 'age', 'email'] 
values=['Nick', '23', 'nick@test.com']

def make_request(keys, values):
    list={}
    if len(values)==len(keys):
        list=dict(zip(keys,values))
        return list
    else:
        return list


print(make_request(keys, values))
    