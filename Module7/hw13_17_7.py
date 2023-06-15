def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        new_list = []
        lines = fh.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            if line:
                if line.find(profession) > 0:
                    repl_str = line.replace(profession, '')
                    # print(repl_str)
                    new_str = repl_str.strip()
                    new_list.append(new_str)
                    stroka = " ".join(new_list)
            else:
                return
        return stroka


path = 'text_13_7.txt'
profession = 'courier'
print(get_employees_by_profession(path, profession))
