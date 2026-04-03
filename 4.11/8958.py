a=int(input())
c=0
e=0
for i in range(a):
    b=input()
    for n in range(len(b)):
        if b[n]=="O":
            c+=e+1
            e+=1
        else:
            e=0
    print(c)
    c=0
    e=0