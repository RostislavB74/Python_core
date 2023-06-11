def total_salary(path):
    import re
    fh = open(path, 'r')
    lines = fh.readlines()
    total = 0.0
    for items in lines:
        salary = re.search(r"(\d+)", items)
        total += float(salary.group())
    fh.close()
    return total


path = 'd:/Users/Rost/Documents/GitHub/module-6/list.txt'
print(total_salary(path))
