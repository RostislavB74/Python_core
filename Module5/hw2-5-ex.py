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
    new_d = []
    if letter_case:
        for d in articles_dict:
            for key_d, val in d.items():
                if str(val).find(key_d) != -1:
                    new_d.append(d)
        return new_d
    else:
        key = key.lower()
        for d in articles_dict:
            for key_d, val in d.items():
                if str(val).lower().find(key) != -1:
                    new_d.append(d)
        return new_d


print(find_articles(key, letter_case=False))
