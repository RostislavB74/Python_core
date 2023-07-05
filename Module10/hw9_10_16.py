from collections import UserDict


class UserDict(UserDict):

    data = dict()


class LookUpKeyDict(UserDict):
    def __init__(self, data, value):
        self.value = value
        self.data = data
        super().__init__(data)

    def lookup_key(self, value, data):
        keys = []
        for key in data:
            if data[key] == value:
                keys.append(key)

        return keys


as_dict = UserDict()
as_dict['a'] = 1
print(as_dict.data())
