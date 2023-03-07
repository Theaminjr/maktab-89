
def range(start = 0 , stop = None ,  step = 1):
    """
    A generator that takes 3 arguments (start,stop,step)\n
    All of the arguments should be integers 
    """   
    if step <= 0 :
        raise Exception ("step cant be a negetive number ")
    if start >= stop:
        raise Exception("Start should be smaller than the stop")
    if type(start) != int or type(stop) != int or type(step) != int:
        raise ValueError
 
    while start < stop :
        start+=step 
        yield start

for i in range(1,8,1):
    print(i)