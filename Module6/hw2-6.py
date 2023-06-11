employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'], ['Drake Mikelsson,19']]
path = 'd:\\Users\\Rost\\Documents\\GitHub\\module-6\\hw2-6.txt'


def write_employees_to_file(employee_list, path):

    fh = open(path, "w")
    for items in employee_list:
        res = print(items)
        # text = fh.write(items)
    fh.close()
    return (res)


write_employees_to_file(employee_list, path)
