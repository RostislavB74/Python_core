import re
from re import search, findall, sub
str = 'лох'
# pattern = '(\b\w+\b)(?=(?:.*?\b\1\b){2,})'
# pattern = r'\s*([А-Яа-яЁё]+)(^\s\.*'
pattern = r'\b'(str)'\b'
string = r'лох - Ты хорош, но вылохглядишь как лох.'
match = re.search(pattern, string)
print(match)
# print(    f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
# print(    f'Группа букв >{match[1]}< с позиции {match.start(1)} до {match.end(1)}'
# print( f'Группа цифр >{match[2]}< с позиции {match.start(2)} до {match.end(2)}')
