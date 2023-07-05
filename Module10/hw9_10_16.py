from collections import UserDict


class UserDict(UserDict):
    data = dict()


class LookUpKeyDict(UserDict):
    
    def lookup_key(self, value):
        keys = []
        for key in data:
            if data[key] == value:
                keys.append(key)

        return keys


as_dict = UserDict()
as_dict['a'] = 1
print(as_dict)
# print(as_dict.lookup_key(1))
