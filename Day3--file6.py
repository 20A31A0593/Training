def fib(n):
   if(n==0):
       return 0
   elif(n==1):
       return 1
   else:
       return (fib(n-1)+fib(n-2))
n=25
i=0
while(i<25):
   x=fib(n)
   i+=1
   print(x,end=" ")