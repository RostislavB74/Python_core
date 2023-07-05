from collections import UserDict, UserList, UserString


class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


as_dict = ValueSearchableDict()
as_dict['a'] = 1
as_dict.has_in_values(1)  # True
as_dict.has_in_values(2)  # False


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
countable.sum()  # 15


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('abcdefghjklmnop')
ts.truncate()
print(ts)  # abcdefg
