num = int(input())
def primecheck(n):
  for i in range(2,n):
      if num % i == 0 :
          return False
  return True

print(primecheck(num))