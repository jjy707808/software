a=int(input())
d={}
for i in range(a):
    c=input().split()
    if c[0] in d:
        del d[c[0]]
    else:
        d[c[0]]=1
x=sorted(d,reverse=True)
for i in range (len(x)):
    print(x[i])