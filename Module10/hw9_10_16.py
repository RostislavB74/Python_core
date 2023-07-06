from collections import UserDict


class UserDict(UserDict):

    data = dict()


class LookUpKeyDict(UserDict):
    def __init__(self, data, value):
        self.value = value
        self.data = data
        super().__init__(data)
        
    def lookup_key(self, key, data):
        keys = []
        for key in data:
            if data[key] == value:
                keys.append(key)
        return keys


as_dict = UserDict()
as_dict['a'] = 1
as_dict['b'] = 2
print(as_dict.data)
key1=LookUpKeyDict()
key1.lookup_key=('v', as_dict)
print(key1.lookup_key())

#keys_list =LookUpKeyDict()

#print(keys_list.lookup_key())
#data1=LookUpKeyDict()
#data1.lookup_key['b']=2


