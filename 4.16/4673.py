def d(n):
    a=0
    n=str(n)
    for i in range(len(n)):
        a+=int(n[i])
    return int(n)+a
c=1
x=[]
y=[]
for i in range(1,10001):
    x.append(d(i))
for i in range(1,10001):
    if i in x:
        pass
    else:
        y.append(i)
for i in range(len(y)):
    if y[i]>10000:
        break
    print(y[i])
    