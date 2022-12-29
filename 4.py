import re
date = "http://www.newspaper.com/edition/20141227.html"

match = re.findall(r"\d{8}",date)
print(f"year {match[-1][0:4]} month {match[-1][4:6]} day {match[-1][6:8]}")