import re
string = "python exercises , c# exercises , c exercises"
print(len(re.findall(r"exercises", string)))
