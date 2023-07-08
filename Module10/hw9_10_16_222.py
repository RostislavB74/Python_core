from collections import UserDict


class UserDict(UserDict):
    # def __init__(self, data):
    data = dict()


class LookUpKeyDict(UserDict):
    # def __init__(self, data):

    #     self.value = value

    def lookup_key(self, data, value):
        super().__init__(data)
        data = data
        value = value
        keys = []
        for i in data:
            print(i)
            if i == value:
                keys.append(i)
        return keys
        # return value in self.data.keys()


as_dict = UserDict()
as_dict['a'] = 1
as_dict['b'] = 2
y = LookUpKeyDict()

print(y.lookup_key(as_dict, 'a'))
