list=[]
flag=0
for i in range(2):
    dict={}
    dict.update({input("Enter Username: "):input("Enter password: ")})
    list.append(dict)
x=input("Enter your username: ")
y=input("Enter your password: ")
temp={x:y}
if temp in list:
    print("Found")
else:
    print("Not found")
