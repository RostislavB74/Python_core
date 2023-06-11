import base64

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']


def encode_data_to_base64(data):
    new64_data = []
    for items in data:

        message_bytes = items.encode("utf-8")
        new64_bytes = base64.b64encode(message_bytes)
        new64_data.append(new64_bytes.decode("utf-8"))

    # print(new64_data)
    return new64_data


print(encode_data_to_base64(data))

# encode_data_to_base64(data)

# message = "Hello world!"
# message_bytes = message.encode("utf-8")
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode("utf-8")

# print(base64_message)  # SGVsbG8gd29ybGQh
