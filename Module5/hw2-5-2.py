import re
from re import search

key = 'Ocean'
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    # if str.istitle(key):
    #    letter_case == True
    #    key_norm = key.lower()
    #    letter_case == False
    # else:
    #    letter_case == False
    #   key_norm = key
    values = []
    new_dict = []
    for items in articles_dict:
        values = items.values()
        for elem in values:
            result = str(elem)
            # result = result1.lower()
            res = re.search(key, result)
            alpha = bool(res)
            if alpha:
                new_dict.append(items)
        continue

    return new_dict


print(key)
print(find_articles(key, letter_case=False))
