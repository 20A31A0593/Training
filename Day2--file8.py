l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(len(l)):
    if(l[i]<0):
        l1.append(l[i])
    else:
        l2.append(l[i])
a=sum(l1)
b=sum(l2)
print(a+b)
print(sum(l))
