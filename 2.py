import re
string = "python exercises , c# exercises , c exercises"
matches = re.finditer(r"exercises", string)
for match in matches :
    print(match.span())