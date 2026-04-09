a=int(input())
c=input().split()
d={}
x=[]
for i in range(len(c)):
    if c[i] in d:
        d[c[i]]+=1
    else:
        d[c[i]]=1
print(d)
z=input()
y=input().split()
for i in range(len(y)):
    if y[i] in d:
        x.append(d[y[i]])
    else:
        x.append("0")
print(*x)
