class Contacts:
    current_id = 1
    

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
         return Contacts.add_contacts.contacts
        

    def add_contacts(self, name, phone, email, favorite=False):
        contacts =[]
        ab={}
        ab['id']= Contacts.current_id
        ab['name'] = name
        ab['phone'] = phone
        ab['email'] = email
        ab['favorite'] = favorite
        contacts.append(ab)
        print (contacts)        

        Contacts.current_id+=1
        print(Contacts.current_id)
        return contacts
        
print (Contacts.list_contacts(Contacts.add_contacts(1,"Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)))
#print(Contacts.add_contacts(1,"Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True))
#print(Contacts.add_contacts(1,"Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True))
#print(Contacts.add_contacts(1,"Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True))
