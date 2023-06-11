users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
path = 'raw_data.bin'


def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key, value in users_info.items():
            # key_utf8 = key.encode('utf-16')
            # print(key_utf8)
            # value_utf8 = value.encode('utf-16')
            # print(value_utf8)
            line = f"{key}: {value}\n"
            # print(type(line))
            fh.write(line.encode('utf-16'))
    return path


save_credentials_users(path, users_info)
