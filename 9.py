import re
string = "salam 1 ami2 man22to"
match = re.finditer("\d+", string)
for m in match:
  print(m.group(),m.span())