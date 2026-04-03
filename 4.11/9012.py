a=int(input())
x=[]
c=0
for i in range(a):
    b=list(input())
    for n in range(len(b)):
        if b[n]=="(":
            for z in range(n,len(b)):
                if b[z]==")":
                    b[z]=0
                    b[n]=0
                    break
    for i in range(len(b)):
        if b[i]!=0:
            c+=1
    if c>0:
        print("NO")
    elif c==0:
        print("YES")
    c=0