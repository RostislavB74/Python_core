import re
text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'


def find_all_emails(text):
    sentence = text.split()
    print(sentence)
    result = []
    for elements in sentence:
        def separate_join(elements):
            elements1 = elements
            separate1 = elements1.split('@')
            separate2 = separate1[1].split('.')
            separate2 = separate2[0:2]
            separate1[1] = '.'.join(separate2)
            elements1 = '@'.join(separate1)

            return elements1
        elements = separate_join(elements)
        if elements and not elements[0].isdigit():
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
