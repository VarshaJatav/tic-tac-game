def show(l1):
    print("\n")
    for i in range(3):
        for j in range(3):
            print(l1[i][j],end="  ")
        print()

import time
import os
os.system('cls')
print("\n\n\n\t\t\t\t------------TIC TAC TOE GAME----------------")
l1=[["-"]*3 for i in range(3)]
name1=input("\n\n\nEnter the name of player1: ")
name2=input("\n\nEnter the name of player2: ")

os.system('cls')
x=0
def fun():
    x=0
    d1={'X':name1,'0':name2}
    for y in d1:
        if (y==l1[0][0]==l1[0][1]==l1[0][2]) or (y==l1[1][0]==l1[1][1]==l1[1][2]) or (y==l1[2][0]==l1[2][1]==l1[2][2]) or (y==l1[0][0]==l1[1][0]==l1[2][0]) or (y==l1[0][1]==l1[1][1]==l1[2][1]) or (y==l1[0][2]==l1[1][2]==l1[2][2]) or (y==l1[0][0]==l1[1][1]==l1[2][2]) or (y==l1[0][2]==l1[1][1]==l1[2][0]):
            x=1       
            print(d1[y]," won")
            exit()
while(x!=1):
    
    show(l1)
    print("\n\n\n\t\t" + name1 + " turn(X): ")
    ans=int(input())
    a,b=ans//10,ans%10
    l1[a][b]="X"
    show(l1)
    fun()

    print("\n\n\n\t\t" + name2 + " turn(0): ")
    ans=int(input())
    a,b=ans//10,ans%10
    l1[a][b]="0"
    fun()
    
print("-----Draw----")
