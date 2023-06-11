import re

regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"

test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"

matches = re.finditer(regex, test_str)

for match in matches:
    print(f"{match.group()} start: {match.start()} end: {match.end()}")
