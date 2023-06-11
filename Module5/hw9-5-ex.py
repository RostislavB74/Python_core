numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
header = '|{:<10}|{:^10}|{:>10}|'.format('decimal', 'hex', 'binary')
body = ''
for num in numbers:
    body += '|{0:<10d}|{0:^10x}|{0:>10b}|\n'.format(num)

table = '\n'.join([header, body])
print(table)
