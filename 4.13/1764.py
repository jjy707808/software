a=list(map(int,input().split()))
d={}
x=[]
for i in range(a[0]+a[1]):
    c=input()
    if c in d:
        x.append(c)
    else:
        d[c]=1
print(len(x))
x.sort()
for i in range(len(x)):
    print(x[i])