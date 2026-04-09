a=int(input())
d={}
x=[]
y=0
for i in range(a):
    c=input()
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for i in d:
    z=int(d[i])
    if z>y:
        y=z
        x.clear
        x.append(i)
    elif z==y:
        x.append(i)
print(x)
x.sort()
print(x[0])