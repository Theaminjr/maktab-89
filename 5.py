import re
from functools import reduce
date = "1400-11-21"
match = re.split(r"-", date)
result = reduce(lambda x , y : x + "-" + y, match[::-1])
print(result)