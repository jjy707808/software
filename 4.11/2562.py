x=[]
for i in range(9):
    x.append(int(input()))
n=max(x)
for i in range(9):
    if n==x[i]:
        b=i
print(n)
print(b+1)