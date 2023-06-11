words = ['banana', 'borsch', 'milk', 'apple', 'pine', 'salo', 'sushi']


gallows = [["-", "|", "- ", "-", "-", " "],
           [" ", "|", " ", " ", "|", " "],
           [" ", "|", " ", " ", " ", " "],
           [" ", "|", " ", " ", " ", " "],
           [" ", "|", " ", " ", " ", " "],
           ["/", " ", "\\", " ", " ", " "]]
gallows[2][4] = "0"
gallows[3][3] = "/"
gallows[3][4] = "|"
gallows[3][5] = "\\"
result = ""
for i in gallows:
    result += "".join(i) + "\n"
print(result)
