
import re


def is_spam_words(text, spam_words, space_around=False):
    if space_around:

        for elem in spam_words:
            reg_exp = r'\b\'' + elem + r'\b\''

            # pattern = rf"'\s{elem}\s'"
            # pattern = '\b'+elem+'\b'
            print(reg_exp)
            # res = re.findall(reg_exp, text)
            res = re.search(reg_exp, text)
            # print(res)
        return bool(res)

    else:
        for elem in spam_words:
            # print(elem)
            # res = re.search(elem, text)
            res = re. findall(elem, text)
            # print(res)
        return bool(res)


# is_spam_words(text, spam_words, space_around=False)
# print(is_spam_words("Мололох ужасен.", ["лох"]))  # True
print(is_spam_words("Молох ужасен.", ["лох"], True))  # False
print(is_spam_words(
    "Ты хорош, но выглядишь как лох.", ["лох"], True))
