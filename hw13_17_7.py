def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        lines = fh.readlines()
    print(lines)


path = 'text_13_7.txt'
profession = 'cook'
get_employees_by_profession(path, profession)
