l1=[]
l2=[]
final_list=[[0 for j in range(2)] for i in range(2)]
for i in range(2):
    x=[]
    for j in range(2):
        x.append(int(input()))
    l1.append(x)

for i in range(2):
    x=[]
    for j in range(2):
        x.append(int(input()))
    l2.append(x)
for i in range(2):
   for j in range(2):
       final_list[i][j]=l1[i][j]+l2[i][j]
       print(final_list[i][j],end=" ")
   print()