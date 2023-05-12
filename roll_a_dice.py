import random
response = "y"
while(response=="y"):
    n = random.randint(1,6)
    print(n)
    print("[-----]")
    if(n==1 or n==2 or n==3
       ):
        print("[     ]")
        if(n==1):
            print("[  0  ]")
        elif(n==2):
            print("[0   0]")
        else:
            print("[0 0 0]")
        print("[     ]")
    else:
        print("[0   0]")
        if(n==4):
            print("[     ]")
        elif(n==5):
            print("[  0  ]")
        else:
            print("[0   0]")
        print("[0   0]")
    print("[-----]")
    print("enter y to continue")
    print("enter n to exit")
    response=input("do you want to roll a dice?")
