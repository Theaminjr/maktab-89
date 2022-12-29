import re
string = "he is on the road to isfahan, not shirazes road"
match = re.sub("road", "rd", string)
print(match)