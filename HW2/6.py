string = "www.google.com"
def check(str):
    freq = {}
    for char in str:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq.update({char:1})
    return freq

print(check(string))


