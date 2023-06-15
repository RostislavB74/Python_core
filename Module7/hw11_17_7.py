phone = {
    1:	['.', ',', '?', '!', ':',],
    2:	['A', 'B', 'C'],
    3:	['D', 'E', 'F'],
    4:	['G', 'H', 'I'],
    5:	['J', 'K', 'L'],
    6:	['M', 'N', 'O'],
    7:	['P', 'Q', 'R', 'S'],
    8:	['T', 'U', 'V'],
    9:	['W', 'X', 'Y', 'Z'],
    0:	[' ']
}


def get_keys_num(bukva):
    bukva = bukva.upper()
    num = ''
    for key, values in phone.items():
        if bukva in values:
            #for j in range(len(values)):
            #    if bukva == values[j]:
            num = str(key)*(values.index(bukva)+1)
                    # print(num)
            return num


def sequence_buttons(string):
    list_string = []
    trans = ''
    for i in string:
        list_string.append(i)
    # print(list_string)
    for j in list_string:
        # print(j)
        trans += get_keys_num(j)

    return trans


string = "Hello, World!"
print(sequence_buttons(string))

        
        