def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fh:
        fh.seek(-1)
        fh.write(additional_info)
    with open(path, 'r') as fh:
        fh.seek(start_pos)
        fh.read(count_chars)


# file_operations(path, additional_info, start_pos, count_chars)
