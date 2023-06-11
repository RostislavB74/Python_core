variable = "abc"

print(r"'" + variable + r"\s'")
print(r"'%s\s'" % variable)
print(r"'{}\s'".format(variable))
print(r"'{x}\s'".format(x=variable))
#print(rf"'{variable}\s'") # не работает в Ideone, Python 3.5
# => 'abc\s'

# Интерполяция и фигурные скобки
print(f"{variable}")
# => abc
print("{{}}".format(variable))
# => {}
print(f"{{variable}}")
# => {variable}
print(f"{{{variable}}}")
# => {abc}