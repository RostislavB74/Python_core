import shutil
# employee_residence={'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
path = 'path/file_name'
file_name = 'file_name'


def create_backup(path, file_name, employee_residence):
    with open(f'{path}/{file_name}', 'wb') as fh:
        for key, value in employee_residence.items():
            line = f"{key} {value}\n"
            fh.write(line.encode('utf-8'))
        archive_name = shutil.make_archive('backup_folder', 'zip', 'folder')
        print(archive_name)
        return archive_name

# create_backup(path, 'file_name', employee_residence)
# def create_backup(path, file_name, employee_residence):
#     with open(path, 'wb') as fh:
#         for key, value in employee_residence.items():
#             line = f"{key} {value}\n"
#             fh.write(line.encode('utf-8'))
#         archive_name = shutil.make_archive('backup_folder', 'zip')
#         return path


# create_backup(path, 'data1.bin', employee_residence)
