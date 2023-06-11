import re
text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org irst_last@iana.org    rst.middle.last@iana.or a@test.com abc111@test.com.net'


def find_all_emails(text):
    sentence = text.split()
    print(sentence)
    result = []
    for elements in sentence:
        if elements and not elements[0].isdigit():
            print(elements[0])
            res = re.findall(
                r"^[a-zA-Z_.+-]+[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+[a-zA-Z]+$", elements)
        else:
            elements = elements[1:]
            res = re.findall(
                r"^[a-zA-Z_.+-]+[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+[a-zA-Z]+$", elements)
        if bool(res):
            result.append(elements)
    return result


print(find_all_emails(text))
# ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', #'first.middle.last@iana.or', 'abc111@test.com']]
# З метою спрощення приймемо, що:

# ми використовуємо для email, — англійський алфавіт
# префікс (все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або букву, включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
# суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві частини, розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два символи (все, що після точки)
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.

# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.
