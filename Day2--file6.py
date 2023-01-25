l=[5,7,9,11,15,19,25,30,49]

key=int(input())
flag=0
for i in range(len(l)):
   if(l[i]==key):
       print(i)
       flag=1
       break

if(flag==0):
   print("Element not found")