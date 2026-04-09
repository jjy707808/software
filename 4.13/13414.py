import sys
input =sys.stdin.readline
a,b=map(int,input().split())
d={}
for i in range (b):
    c=input().strip()
    d[c]=i
x=sorted(d,key=lambda k:d[k])
print(x)
for i in range(a):
    print(x[i]) 