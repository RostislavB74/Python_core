user = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}


new_list = []


def get_emails(list_contacts):
    # for i in map(lambda elem: new_list.append(elem['email']), user):
    for i in map(if elem[0] == "email": print(elem), list_contacts.items()):
        print()
        # print(new_list)

        # return (new_list)


print(get_emails(user))
