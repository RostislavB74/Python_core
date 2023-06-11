# def is_equal_string(utf8_string, utf16_string):
s = "Привет!"
# utf8 = s
# utf16 = s.encode('utf-16')
# result = s.casefold()


def is_equal_string(utf8_string, utf16_string):

    str_utf8 = utf8_string.casefold()
    str_utf16 = utf16_string.casefold()
    utf8 = str_utf8.encode('utf-8')
    utf16 = str_utf16.encode('utf-16')
    s_from_utf16 = utf16.decode('utf-16')
    s_from_utf8 = utf8.decode('utf-8')
    print(utf8)
    print(utf16)

    return s_from_utf8 == s_from_utf16


print(is_equal_string(s, s))

# print(utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'


# print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)  # True
# print(b'Hello world!'.decode('utf-16'))  # 效汬潷汲Ⅴ
