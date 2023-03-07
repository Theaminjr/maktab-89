def validate(x):
    x = x.split()
    if len(x) != 3:
        raise Exception("You need exactly 3 inputs seperated by whitespaces")
    for i in x[0]+x[2]:
        if i not in ["0","1","2","3","4","5","6","7","8","9","."] :
            raise Exception("num1 and num2 should be numbers (float or integer)")
    if x[1] not in ["*","/","+","-","%"]:
        raise Exception("enter a valid operator(+ , - , * , / , %)")
    return True