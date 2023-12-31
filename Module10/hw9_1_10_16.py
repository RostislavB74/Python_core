from collections import UserDict


class UserDict(UserDict):
    data = dict()


class LookUpKeyDict(UserDict):
    def __init__(self, data, value):
        super().__init__(data)
        self.value = value

    def lookup_key(self, data, value):
        keys = []
        for i in data:
            # print(i)
            if i == value:
                keys.append(i)
        return keys
        # return value in self.data.keys()


as_dict = UserDict()
as_dict['a'] = 1
as_dict['b'] = 2
# print(as_dict)
y = LookUpKeyDict(data=None, value=None)
# y.LookUpKeyDict.lookup_key=(as_dict,'v')
print(y.lookup_key(as_dict, 'a'))
