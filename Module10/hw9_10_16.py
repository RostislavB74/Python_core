from collections import UserDict


class UserDict(UserDict):
    # def __init__(self, data):
    data = dict()


class LookUpKeyDict(UserDict):
    def __init__(self, value):
        super().__init__(dict)
        self.value = value
        self.data = dict

    def lookup_key(self, data, value):
        keys = []
        for i in self.data:
            print(i)
            if i == value:
                keys.append(i)
        return keys
        # return value in self.data.keys()


as_dict = UserDict()
as_dict['a'] = 1
as_dict['b'] = 2
y = LookUpKeyDict()
y.lookup_key = (as_dict, 'v')
print(y.lookup_key())
