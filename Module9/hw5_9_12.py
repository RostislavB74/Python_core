# phone = ("    +38(050)123-32-34",
#          "     0503451234",
#          "(050)8889900",
#          "38050-111-22-22",
#          "38050 111 22 11   ",)


def format_phone_number(sanitize_phone_number):
    def simple_wrapper(phone):

        result = sanitize_phone_number(phone)
        if len(result) < 12:
            modif_phone = '+38'
        if len(result) == 12:
            modif_phone = '+'

        if result[0] == '+' and len(result) == 13:
            return result

        return modif_phone+result
    return simple_wrapper


@format_phone_number
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


result = sanitize_phone_number(phone)
