

history =""
def dictostring(d): #this function turns dictionary to a sorted string
    string=""
    result=""
    global history
    for i in d.keys() : #turn the dictionary to a string
        string = string +i+str(d[i]) if d[i] != 1 else string + i
    for x in sorted(string): #sort the string
        result += x
    if result == history: #check if the result is repeated
        return True
    else:
        history = result
        print(result)
        check(result)







def check(n): # creates a dictinary with numbers as keys and repetition as values
    nums = {}
    for i in n:
        if i in nums:
            nums[i] = nums[i] + 1
        else:
            nums.update({i:1})
    dictostring(nums)
    


num = input()
check(num)

