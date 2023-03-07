clist = [0,22,30,44]
flist=[]
def ctof (c):
     f=(c*9/5)+32
     return f

flist = list(map(ctof,clist))
print(flist)