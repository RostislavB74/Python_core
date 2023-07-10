class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        self.contacts.append(Contacts.add_contacts())
        return self.contacts

    def add_contacts(key,name, phone, email, favorite=False):
        ab={}
        key = Contacts.current_id
        contacts =[]
        while True:
            
            ab['id']= key
            ab['name'] = name
            ab['phone'] = phone
            ab['email'] = email
            ab['favorite'] = favorite
            
            key+=1
            return ab
        #self.contacts.id = self.current_id


print(Contacts.add_contacts(1,"Wylie Pope", "(692) 802-2949", "est@utquamvel.net", favorite =True))

#    {
#     "id": 1,
#     "name": "Wylie Pope",
#     "phone": "(692) 802-2949",
#     "email": "est@utquamvel.net",
#     "favorite": True,
# }              
# users=[{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True}, {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]

# def is_favorite(elem):
#     if elem['favorite']:
#         return elem


# def get_favorites(contacts):
#     # new_list = []
#     # for i in (lambda i: i.get('favorite'), users):
#     #     return i
#     list1 = filter(is_favorite, contacts)
#     return list(list1)


# print(get_favorites(users))  