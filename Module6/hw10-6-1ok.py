users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
path = 'raw_data.bin'


def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key, value in users_info.items():
            line = f"{key}:{value}\n"
            fh.write(line.encode('utf-8'))
    return path


save_credentials_users(path, users_info)
