import re
list_phones = ["+81(050)123-32-34", "     +650503451234",
               "+88(650)8889900", "38050-111-22-22", "+38050 111 22 11   ",]


def get_phone_numbers_for_countries(list_phones):
    new_phone = []
    UA = []
    SG = []
    TW = []
    for phone in list_phones:

        def sanitize_phone_number(phone):
            new_phone = (
                phone.strip()
                .removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                .replace(" ", "")
            )
            return new_phone

        # JP.append(new_phone.find('81'))
        # SG.append(new_phone.find('65'))
        # TW.append(new_phone.find('886'))
        UA.append(sanitize_phone_number(phone))

    # return {"JP": JP, "SG": SG, "TW": TW}
    return UA


print(get_phone_numbers_for_countries(list_phones))
