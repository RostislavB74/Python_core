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
    values = []
    new_dict = []
    if letter_case:
        for items in articles_dict:
            values = items.values()
            for elem in values:
                result = str(elem)
                res = re.search(key, result)
                alpha = bool(res)
                if alpha:
                    new_dict.append(items)
            continue

        return new_dict
    else:
        key_norm = key.lower()
        for items in articles_dict:
            values = items.values()
            for elem in values:
                result1 = str(elem)
                result = result1.lower()
                res = re.search(key_norm, result)
                alpha = bool(res)
                if alpha:
                    new_dict.append(items)
            continue

        return new_dict


print(find_articles('Oceans', True))
