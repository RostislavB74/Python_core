applicant = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
source = applicant
output = 'text-ex.txt'


def save_applicant_data(source, output):
    with open(output, 'w') as file:
        for applicant in source:
            line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
            file.write(line)
    return output


# file = open('text.txt', 'w')
# for key, value in a.items():
#   file.write(f'{key}, {value}\n')
# file.close()
save_applicant_data(source, output)
