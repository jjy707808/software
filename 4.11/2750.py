a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(len(b)):
    for n in range(len(b)):
            c+=abs(b[i]-b[n])
    print(c)
print(c)