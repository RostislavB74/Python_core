import shutil
archive_path = 'archive_path'
path_to_unpack = 'path_to_unpack'


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)


unpack(archive_path, path_to_unpack)
