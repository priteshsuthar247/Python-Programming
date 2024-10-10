import random
def conditional_control_structures():
    print("Conditional Control Structures")
    x = random.randrange(0,100,5)
    y = random.randrange(0,100,5)
    z = random.randrange(0,100,5)
    print("Value of X,Y,Z are:",x,y,z)
    if x>y or x>z:
        print(x,"is the largest")
    elif x<y:
        print(y,"is the largest")
    else:
        print(z,"is the largest")

def loop_structures():
    print("Loop Structures")
    x = random.randrange(0,100,5)
    
    print("Value of X is:",x)
    for i in range(x,10,-10):
        print(i,end=" ")
    print("")

    y = random.randrange(0,100,5)
    print("Value of Y is:",y)
    while(y>10):
        print(y,end=" ")
        y-=10
    print("")

def break_statement():
    print("Break Statement")
    for i in range(0,10):
        print("Value of i is:",i)
        break

def continue_statement():
    print("Continue Statement")
    for i in range(0,10):
        if i==5:
            continue
        else:
            print(i, end=" ")
    print("")

def pass_statement():
    print("Pass Statement")
    str = "Hi"
    for i in str:
        if i =='i':
            print("o")
            pass
        print(i)
        
conditional_control_structures()
print("")
loop_structures()
print("")
break_statement()
print("")
continue_statement()
print("")
pass_statement()