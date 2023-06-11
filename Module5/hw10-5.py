import re


def find_word(text, word):
    text1 = text.lower()
    word1 = word.lower()
    # res = re.search(word, text)
    # match.start() == None
    # match.end() == None
    match = re.search(word1, text1)
    if match:
        # match.groups(default=None)
        print(match.group())
        match.span()
        match.start()
        match.end()

        total = {'result': bool(match), 'first_index': match.start(),
                 'last_index': match.end(),
                 'search_string': match.group(),
                 'string': text
                 }
        return total
    else:

        total = {'result': bool(match), 'first_index': None,
                 'last_index': None,
                 'search_string': word,
                 'string': text
                 }
        return total


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Pyuu"))

# """При виклику функції:
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
# Результат має бути наступного виду при збігу:
# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
# {
#     'result': False,
#     'first_index': None,
#     'last_index': None,
#     'search_string': 'python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }

#    result — результат пошуку True або False
# first_index — початкова позиція збігу
# last_index — кінцева позиція збігу
# search_string — частина рядка, в якому був збіг
# string — рядок, переданий у функцію
# Якщо збігів не виявлено:

#     """
