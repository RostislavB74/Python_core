class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.startswith("01"):
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException
    
    while True:
        try:
            employee_id= employee_id
            break
        except IDException:
            print('Name start with 01 Try again.')
    