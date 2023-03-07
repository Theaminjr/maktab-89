

def clean(x):  # deletes special characters from a file and returns cleanded string
  str=""
  with open(x) as f:
    for line in f:
      for letter in line:
        if not 65 <= ord(letter.upper()) <= 90:
          str += " " 
        else :
            str += letter
    return str
    
    
def findupper(str): # takes a string and gives a lists of words starting with uppercase
    uppers = []
    for i in str.split():
        if i[0].isupper() and i not in uppers:
            uppers.append(i)
    return uppers


def writelisttofile(l,f): #takes list and file. then writes the list to the file
    with open(f,"a") as f:
        for item in l :
            f.write(f"{item}\n")




cleaned = clean("iran.txt")
uppers = findupper(cleaned)
writelisttofile(uppers,"upper.txt")
