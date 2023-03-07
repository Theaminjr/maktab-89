num = int(input())
x=0
for i in range(1,num):
    if num%i==0 and i < num:
        x = x+i

if x == num:
    print("YES")
else:
    print("NO") 