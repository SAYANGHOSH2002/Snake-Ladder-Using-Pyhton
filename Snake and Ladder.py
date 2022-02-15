import random

def check(num):
    if num==83 or num==62 or num==47 or num==15:
        return num-10
    elif num==55 or num==78 or num==22:
        return num-20
    elif num==95:
        return 37
    elif num==20 or num == 39 or num ==64:
        return num+15
    elif num==49 or num == 37 or num==9:
        return num+8
    elif num==25:
        return 62
    else:
        return num

def player1(p1,n,s1):
    
    print("\n",p1, "'s turn: ")
    while(True):
        print("1. Want to play\n2. Quit")
        c1=int(input("Enter Your Choice: "))
        if c1==1:
            r=random.randint(1,6)
            if s1+r > n:
                print("Dice: ",r,"\n","Total: ",s1+r,"\n N.A.")
                break
            else:
                print("Dice: ",r)
                s1=s1+r
                num=check(s1)
                if num > s1:
                    print("Total: ",s1,"\nLadder\n Total: ",num)
                    s1=num
                elif num < s1:
                    print("Total",s1,"\nSnake\n Total: ",num)
                    s1=num
                else:
                    print("Total: ",s1)
                break
        elif c1==2:
            print("Quitting!!")
            return exit()
        else:
            print("Wrong choice\nTry again!!")
    if s1 == n:
        print(p1," wins!!\nCongratulations!!")
        c3=input("Press any key to exit")
        return exit()
    return s1

def player2(p2,n,s2):
    
    print("\n",p2,"'s turn: ")
    while(True):
        print("1. Want to play\n2. Quit")
        c2=int(input("Enter your choice: "))
        if c2==1: 
            r=random.randint(1,6)
            if s2+r>n:
                print("Dice: ",r,"\n","Total: ",s2+r,"\n N.A.")
                break
            else:
                print("Dice: ",r)
                s2=s2+r
                num=check(s2)
                if num>s2:
                    print("Total: ",s2,"\nLadder\n Total: ",num)
                    s1=num
                elif num<s2:
                    print("Total: ",s2,"\nSnake\n Total: ",num)
                    s1=num
                else:
                    print("Total: ",s2)
                break
        elif c2==2:
            print("Quitting!!")
            return exit()
        else:
            print("Wrong choice\nTry again")
    if s2 == n:
        print(p2," wins!!\nCongratulations!!")
        c3=input("Press any key to exit")
        return exit()
    return s2


print("------------Welcome to Ludo------------")
p1=input("Enter name of the 1st Player: ")
p2=input("Enter name of the 2nd Player: ")
n=100
s1=0
s2=0

while(True):
    s1=player1(p1,n,s1)
    s2=player2(p2,n,s2)
