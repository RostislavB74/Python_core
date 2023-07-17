import json
import sys
contacts= {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}
#contacts = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
filename = 'data.json'
def write_contacts_to_file(filename, contacts):
    pack={}
    pack['contacts'] = contacts
    with open(filename, "w") as fh:
        json.dump(pack, fh)
        


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        
        return json.load(fh)

write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))