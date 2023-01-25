from random import random,randint
p1=0
p2=0
print("Menu: \n rock \n paper \n scissors")
print("Enter your choice:")
while(p1<5 or p2<5):
    x=input("Player1: ")
    player1=0
    if(x=="rock"):
        player1=0
    elif(x=="paper"):
        player1=1
    elif(x=="scissors"):
        player1=2
    player2=randint(0,2)
    if(player2==0):
        print("Player2: rock")
    elif(player2==1):
        print("Player2: paper")
    elif(player2==2):
        print("Player2: scissors")
    if(player1==0):
        if(player2==1):
           p2+=1
        elif(player2==2):
           p1+=1
        elif(player2==0):
           pass
    elif(player1==1):
        if(player2==0):
           p1+=1
        elif(player2==2):
           p2+=1
        elif(player2==1):
           pass
    elif(player1==2):
        if(player2==0):
           p2+=1
        elif(player2==1):
           p1+=1
        elif(player2==2):
           pass
    else:
        print("Invalid Input")
    print("Player1 Score:",p1,"   Player2 Score:",p2)
if(p1==5):
    print("Player1 won")
elif(p2==5):
    print("Player2 won")

