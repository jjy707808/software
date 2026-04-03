a=int(input())
c=0
x=[]
for i in range(a):
    b=int(input())
    if b==0:
        del x[-1]
    else:
        x.append(b)
if len(x)==0:
    print(0)
else:
    for i in range(len(x)):
        c+=x[i]
    print(c)