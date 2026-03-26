a=int(input())
b=[]
for i in range(a):
    x,y=map(int,input().split())
    b.append(x+y)
for i in range(len(b)):
    print(b[i])