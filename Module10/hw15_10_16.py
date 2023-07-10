contacts = [{'id': 1, 'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
            {'id': 2, 'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca',
                'phone': '(294) 840-6685', 'favorite': False},
            {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net',
             'phone': '(542) 451-7038', 'favorite': True},
            {'name': 'Wylie Pope', 'email': 'est@utquamvel.net',
             'phone': '(692) 802-2949', 'favorite': False},
            {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        self.id = id
        for elem in self.contacts:

            if elem.get(self.id, 'id'):
                return elem
            return
