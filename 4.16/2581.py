a=int(input())
b=int(input())
x=[]
c=0
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            c+=1
    if i ==1:
        c=100
    if c==0:
        x.append(i)
    c=0
if len(x)>0:
    print(sum(x))
    print(min(x))
else:
    print(-1)