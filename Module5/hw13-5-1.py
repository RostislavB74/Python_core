import re
# text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org    first.middle.last@iana.or a@test.com abc111@test.com.net'
text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'


def find_all_emails(text):
    sentence = text.split()
    # print(sentence)
    result = []
    for elements in sentence:

        if elements and not elements[0].isdigit():
            # print(elements[0])
            res = re.findall(
                r"^[a-zA-Z_0-9_.+-]+[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+[a-zA-Z]+$", elements)
        else:
            elements = elements[1:]
            res = re.findall(
                r"^[a-zA-Z_.+-]+[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+[a-zA-Z]+$", elements)
        if bool(res):
            result.append(elements)
    return result


print(find_all_emails(text))
