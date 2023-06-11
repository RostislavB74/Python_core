path = 'raw_data.bin'


def get_credentials_users(path):
    line = []
    with open(path, 'rb') as fh:
        while True:
            str_1 = fh.readline()
            str_1 = str_1.decode('utf-8').rstrip('\n')

            if not str_1:
                break
            line.append(str_1)
            # print(line)
      # while True:
        return line


print(get_credentials_users(path))
