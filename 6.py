import re

words = ["ali","pride","kazem","pari","hamid","poori"]

found = []
for name in words:
    if re.search("^p", name) and len(found) < 2:
        found.append(name)
print(found)
