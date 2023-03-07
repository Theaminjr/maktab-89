string = input()
new_string =""
for char in string:
    if char == " ":
        new_string = new_string + ""
    if char in ["a","e","i","o","u"]:
        new_string = new_string + "."
    elif char.isupper():
        new_string = new_string + char.lower()
    elif char.islower():
        new_string = new_string + char.upper()
print(new_string)