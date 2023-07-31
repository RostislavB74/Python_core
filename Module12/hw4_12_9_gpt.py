import pickle

filename = 'user_class.dat'


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts): #:list[Person] = None):
        self.filename = filename
        self.contacts = contacts if contacts is not None else []

    def save_to_file(self):
        encoded = pickle.dumps(self)
        print(encoded)
        with open(self.filename, "wb") as fh:
<<<<<<< HEAD
            pickle.dump(self, fh)
=======
            fh.write(encoded)
>>>>>>> e65f8bf0ece7d7fb6542c44255115f5d7660be42

    def read_from_file(self):
        with open(self.filename, "rb") as f:
            unpacked_contacts = pickle.load(f)
        return unpacked_contacts


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
for person in person_from_file:
    print(person.name, person.email, person.phone, person.favorite)
print(f"persons_posle{person_from_file}")
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
