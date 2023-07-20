import pickle

filename = 'user_class.dat'
class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name   
        self.email= email
        self.phone = phone
        self.favorite = favorite
        
        
        
        

class Contacts:
    def __init__(self, filename: str, contacts):
        self.filename = filename
        self.contacts = contacts
        if self.contacts is None:
            self.contacts = []
        
        

    def save_to_file(self):
        with open(filename, "wb") as fh:
            pickle.dump(self.contacts, fh)
        
    def read_from_file(self):
        with open(filename, "rb") as fh:
            unpack_contacts = pickle.load(fh) 
            return unpack_contacts
            
                

contacts = [
    Person("Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False, ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]    
persons = Contacts(filename, contacts)
print(f"persons_do{persons}")

#persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(f"persons_posle{person_from_file}")
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
#print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
#print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
#print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True