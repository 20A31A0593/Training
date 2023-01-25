l=[0,1]
i=2
while(i<=25):
   l.append(l[i-1]+l[i-2])
   i+=1
print(l)