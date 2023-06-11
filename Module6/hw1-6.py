import os
import re

fh = open('list.txt', 'r')
# some_useful_function(fh)
lines = fh.readlines()
total = 0.0
for items in lines:
    salary = re.search(r"(\d+)", items)
    total += float(salary.group())
print(total)
fh.close()
