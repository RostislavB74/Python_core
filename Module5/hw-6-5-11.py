import re


def is_spam_words(text, spam_words, space_around=False):

    text1 = text.lower()
    if space_around:

        for elem in spam_words:
            elem = elem.lower()
            print(elem)

            pattern = fr"\b{elem}\b"
            print(pattern)
            res = re.search(pattern, text1)

        return (bool(res))

    else:
        for elem in spam_words:
            elem = elem.lower()
            res = re. findall(elem, text1)

        return (bool(res))


print(is_spam_words("Мололох ужасен.", ["лох"]))  # True
print(is_spam_words("Молох ужасен.", ["лох"], True))  # False
print(is_spam_words(
    "Ты хорош, но выглядишь как лох.", ["Лох"], True))
