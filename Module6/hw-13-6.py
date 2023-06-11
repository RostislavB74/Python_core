import shutil

employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}

path = 'data1.bin'

file_name = 'data1.bin'

archive_name = 'backup_folder.zip'


def create_backup(path, file_name, employee_residence):
    with open(path, 'wb') as fh:
        for key, value in employee_residence.items():
            line = f"{key} {value}\n"
            fh.write(line.encode('utf-8'))
        archive_name = shutil.make_archive('backup_folder', 'zip')

    shutil.unpack_archive(
        archive_name, 'D:\\Users\\Rost\\Documents\\GitHub\\module-6\\new_folder\\')
    return archive_name


print(create_backup(path, file_name, employee_residence))
