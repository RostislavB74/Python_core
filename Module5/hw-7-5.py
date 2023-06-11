CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
CYRILLIC = []
TRANS = {}
for i in range(len(CYRILLIC_SYMBOLS)):
    CYRILLIC.append(CYRILLIC_SYMBOLS[i])
print(CYRILLIC)
print(len(CYRILLIC), len(TRANSLATION))
for c, l in zip(CYRILLIC, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    # TRANSLIT_DICT[ord(c)] = l
    # TRANSLIT_DICT[ord(c.upper())] = l.upper()
#
# TRANS[ord(c.upper())] = l.upper()
# print(TRANS)


def translate(name):
    return name.translate(TRANS)


print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
