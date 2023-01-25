n=int(input("Enter a number: "))
if((n>0) and (n<20)):
    if((n%2)==0):
        print("Weird Number")
    else:
        print("Normal Number")
elif(n>=20 and n<30):
    print("Normal Number")
elif(n>=30):
    if((n%2)==0):
        print("Weird Number")
    else:
        print("Normal Number")
   
