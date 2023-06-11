def formatted_numbers():

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    body = []
    table = []
    body.append('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))
    for num in numbers:
        body.append('|{0:<10d}|{0:^10x}|{0:>10b}|'.format(num))

    return body


for el in formatted_numbers():
    print(el)
