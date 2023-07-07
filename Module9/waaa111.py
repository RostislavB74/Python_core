users=[{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': False}, {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}] 

def get_emails(list_contacts):
    new_list=[]
    for elem in list_contacts:
        new_list.append(elem['email'])
    return new_list
def add_email(users):
    res =get_emails(users)
    return res 
print(add_email(users))



# def square(number):
# ...       return number ** 2
# ...
# >>> numbers = [1, 2, 3, 4, 5]
# >>> squared = map(square, numbers)
# >>> list(squared)
# [1, 4, 9, 16, 25]