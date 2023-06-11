replace_dict = {117: "o"}
txt = "sun"
print(txt.translate(replace_dict))  # son
replace_dict = {ord("u"): "o"}
txt = "sun"
print(txt.translate(replace_dict))  # son
txt = "sun"
my_table = txt.maketrans("u", "o")
print(txt.translate(my_table))  # son
txt = "sun"
my_table = txt.maketrans("nus", "mot")
print(txt.translate(my_table))  # tom
txt = "the sun"
my_table = txt.maketrans("nus", "nos", "he t")
print(txt.translate(my_table))  # son
# CYRILLIC = ("а", "ч", "ш")
# LATIN = ("a", "ch", "sh")
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print("Дмитро Короб".translate(TRANSLIT_DICT))  # chasha
print("Олекса Івасюк".translate(TRANSLIT_DICT))  # CHASHA
# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
