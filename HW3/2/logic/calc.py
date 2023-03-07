def calc(x):
    num1,num2,operator = x
    if operator == "*":
        return num1 * num2
    elif  operator == "/":
        return num1 / num2
    elif  operator == "+":
        return num1 + num2
    elif  operator == "-":
        return num1 - num2
    elif  operator == "%":
        return num1 % num2