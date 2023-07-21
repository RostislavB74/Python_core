import pickle

filename = 'user_class.dat'


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts=None):
        self.filename = filename
        self.contacts = contacts if contacts is not None else []

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self.contacts, fh)

    def read_from_file(self):
        with open(self.filename, "rb") as f:
            unpacked_contacts = pickle.load(f)
        return Contacts(self.filename, unpacked_contacts)  # Wrap the data in Contacts class


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
persons = Contacts(filename, contacts)

persons.save_to_file()
person_from_file = persons.read_from_file()

# Now, let's check if the data is correctly loaded from the file:
#print(person_from_file.contacts[0].name)  # Allen Raymond
#print(person_from_file.contacts[0].email)  # nulla.ante@vestibul.co.uk
#print(person_from_file.contacts[0].phone)  # (992) 914-3792
#print(person_from_file.contacts[0].favorite)  # False

# Now, the comparison will return True
print(persons == person_from_file)  # True
print(persons.contacts[0] == person_from_file.contacts[0])  # True
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
