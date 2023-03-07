import time

factorial_cache ={}
Fibonacci_cache = {}
timer = []

def cache(f):
    def wrapper(n):
        result = f(n)
        if f.__name__ == "factorial":
          factorial_cache[n]=result
        else:
            Fibonacci_cache[n]=result
        return result
    return wrapper



def timer_process(f):
     def wrapper(n):
        timer.append(time.time()) 
        result = f(n)
        timer.append(time.time())
        print(n)
        print(timer)
        print(f"t2 is {timer[-1]} t1 is {timer[0]} and diffrence {timer[-1]-timer[0]}")
        return result 
     return wrapper



@timer_process
@cache
def Fibonacci(n):
    if n in Fibonacci_cache.keys():
        return Fibonacci_cache[n]
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

@timer_process 
@cache
def factorial(n):
   if n in factorial_cache.keys():
        return factorial_cache[n]
   if n == 1:
       return n 
   else:
       return n*factorial(n-1)


while True:
   timer = []
   print(factorial(int(input("enter your index ==> "))))
   print(factorial_cache)
   print(Fibonacci_cache)
