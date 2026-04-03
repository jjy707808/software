x=[]
for i in range(10):
    a=int(input())
    x.append(a%42)
c=set(x)
print(len(c))
