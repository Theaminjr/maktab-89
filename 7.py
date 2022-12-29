import re
string = "salam 1 ami2 man22to"
match = re.findall("\d+", string)
print(match)