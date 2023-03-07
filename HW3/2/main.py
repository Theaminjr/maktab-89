from exceptions import validate
from logic.parse import parse
from logic.calc import calc
_input ="" 
while True:
   _input = input("{num1} {operator} {num2} ==> ")
   try: 
       flag =  validate(_input)
   except Exception as error:
        print(error)
        flag = False
   if flag == True:
       result = calc(parse(_input))
       print(result)
       with open("history.txt","a") as hs:
         log = f"{_input} = {result}\n"
         hs.write(log)
         

