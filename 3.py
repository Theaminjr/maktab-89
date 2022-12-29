import re
string= "python exer_cises , c# ex_ercises , c exercises"
string = re.sub(r" ", "1", string)
string = re.sub(r"_", " ", string)
string = re.sub(r"1", "_", string)

print(string)
