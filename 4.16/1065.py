a=int(input())
c=0
y=0
for i in range(1,a+1):
    if i<100:
        c+=1
    else:
        i=str(i)
        for j in range(len(i)-2):
            if int(i[j+1])-int(i[j])==int(i[j+2])-int(i[j+1]):
                c+=1
                y+=1
        if y>=1:
            c-=len(i)-3
            y=0
print(c)