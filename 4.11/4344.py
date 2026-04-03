num1=int(input())
count=0
x=[]
u=[]
c=0
for n in range(num1):
    x=list(map(int, input().split()))
    for z in range(1,len(x)):
        count+=x[z]
    av=count/x[0]
    for y in range(1,len(x)):
        if av<x[y]:
            c+=1
    u.append(f"{c/x[0]*100:.3f}")
    x.clear()
    count=0
    av=0
    c=0
for i in range(len(u)):
    print(f"{u[i]}%")