import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        ...


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []

    def save_to_file(self):
        with open(filename, "wb") as fh:
            pickle.dump(contacts, fh)

    def read_from_file(self):
        with open(filename, "rb") as fh:
            unpack_contacts = pickle.load(fh)


filename = "user_class.dat"
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
persons.save_to_file()
# bob = Human("Bob")
# encoded_bob = pickle.dumps(bob)

# decoded_bob = pickle.loads(encoded_bob)
# persons = Contacts("user_class.dat", contacts)
