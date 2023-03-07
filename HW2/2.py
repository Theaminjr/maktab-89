from functools import reduce 
nums = [8, 2, 3, -1,7]
total = reduce(lambda x, y: x * y, nums)
print(total) 