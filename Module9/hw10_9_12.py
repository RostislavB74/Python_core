users = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True}, {
    'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]


def is_favorite(elem):
    if elem['favorite']:
        return elem


def get_favorites(contacts):
    # new_list = []
    # for i in (lambda i: i.get('favorite'), users):
    #     return i
    list1 = filter(is_favorite, contacts)
    return list(list1)


print(get_favorites(users))
# def is_positive(num):
#     return num >= 0


# def positive_values(payment):
#     list1 = filter(is_positive, payment)
#     return list(list1)


# print(positive_values(payment))
