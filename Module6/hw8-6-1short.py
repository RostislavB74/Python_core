source = [
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
output = 'output8.txt'


def save_applicant_data(source, output):
    with open(output, 'w') as file_output:
        # for dicts in source:
        #     file_output.write(','.join([str(item) for item in dicts.values()]))
        #     file_output.write('\n')

        line_list = []
        result = ''
        for items in source:
            for value in items.values():
                line_list.append(str(value))

            result = ",".join(line_list)

        print(result)
        file_output.write(result)

    return


save_applicant_data(source, output)
