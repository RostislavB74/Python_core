from collections import UserDict


class UserDict(UserDict):
    data = dict()


class LookUpKeyDict(UserDict):
    def __init__(self, value, data):
        super().__init__(data)
        self.value = value

    def lookup_key(self, data, value):
        keys = []
        for i in data:
            # print(i)
            if i == value:
                keys.append(i)
        return keys


as_dict = UserDict()
as_dict = {'a': 1, "b": 2}
y = LookUpKeyDict(None, None)
print(y.lookup_key(as_dict, 'b'))
