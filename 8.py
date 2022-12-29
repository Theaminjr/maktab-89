import re
string = "amin raft noon bekhare ehsan oomad pish emad va ali"
match = re.findall(r"\b[aeAE]\w*\b", string)
print(match)