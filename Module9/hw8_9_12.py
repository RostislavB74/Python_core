user = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}


new_list = []


def get_emails(list_contacts):
    for elem in list_contacts:
        print(elem)
        if elem =='email':
            new_list.append(list_contacts['email'])
    return(new_list)

                #    result = map(user, ('992', user.items()))
    #    print(result)
    #for i in map(lambda keys, value: new_list.append(value, user) if keys=='email'in list_contacts.items())
        #print(new_list)
        # print(new_list)

        # return (new_list)


print(get_emails(user))
