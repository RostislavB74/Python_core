users=[{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': False}, {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}] 

def get_emails(list_contacts):
    new_list=[]
    for elem in list_contacts:
        return elem['email']
# def add_email(users):
res= map(get_emails,users)
list (res)     #print(res)
# def square(number):
# ...       return number ** 2
# ...
# >>> numbers = [1, 2, 3, 4, 5]
# >>> squared = map(square, numbers)
# >>> list(squared)
# [1, 4, 9, 16, 25]



# def is_positive(num):
#    return num >= 0

# def sanitized_sqrt(numbers):
#      cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
#      return list(cleaned_iter)

# sanitized_sqrt([25, 9, 81, -16, 0])