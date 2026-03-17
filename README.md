a=int(input())
b=int(input())
c=int(input())
e=int(input())
f=int(input())
y=3000
z=3000
x=[a,b,c]
drink=[e,f]
for i in range(3):
    if y>x[i]:
        y=x[i]
for i in range(2):
    if z>drink[i]:
        z=drink[i]
print(y+z-50)
