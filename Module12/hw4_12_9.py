import pickle
filename = 'user_class.dat'

filename = 'user_class.dat'
class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
        return self
        
        
        

=======

>>>>>>> 00e278bfe81f0c45f023770e1b5ff9a0d2f27c29

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        self.file = open(filename)
        self.contacts = contacts
        if self.contacts is None:
            self.contacts = []

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self.contacts, fh)

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            unpack_contacts = pickle.load(fh) 
        return unpack_contacts        

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]    
persons = Contacts("user_class.dat", contacts)