import shutil

# archive_name = shutil.make_archive('backup', 'zip')


# archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')


# archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')
# shutil.unpack_archive(archive_name, 'new_folder_for_data')
for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))
