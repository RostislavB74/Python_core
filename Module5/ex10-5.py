import re
s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'>
s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25

statement = r'new (car)|old (car)'
text = 'I bought a new car and got rid of the old car'
match = re.search(statement, text)
match.start()
match.end()
match.span()
print(f'mgroup = {match.group()}')
# Out: (11, 18)
print(match.group(0))
for match in re.finditer(statement, text):
    print(match.start())
    print(match.end())

    print(match.span())
# Out: (11, 18)
# Out: (38, 45)
