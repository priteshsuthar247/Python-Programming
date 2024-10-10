def arithmetic_operators():
    import random
    x = random.randrange(0,100,5)
    y = random.randrange(0,100,5)
    print("Arithmetic Operations in Python")
    print("Addition of",x,"and",y,"is:",x+y)
    print("Subtraction of",x,"and",y,"is:",x-y)
    print("Multiplication of",x,"and",y,"is:",x*y)
    print("Division of",x,"and",y,"is:",x/y)
    print(x,"Modulo",y,"is:",x%y)
    print(x,"raised to",y,"is:",x**y)
    print("Floor division of",x,"and",y,"is:",x//y)

def assignment_operators():
    import random
    x = random.randrange(0, 100, 5)
    print("Assignment Operations in Python")
    y=x; x += 5
    print(f"The final result of {y} += 5 is:", x)
    y=x; x -= 3
    print(f"The final result of {y} -= 3 is:", x)
    y=x; x *= 2
    print(f"The final result of {y} *= 2 is:", x)
    y=x; x /= 4
    print(f"The final result of {y} /= 4 is:", x)
    y=x; x %= 1
    print(f"The final result of {y} %= 1 is:", x)
    y=x; x //= 2
    print(f"The final result of {y} //= 2 is:", x)
    x = random.randrange(0,100,5)
    y=x; x **= 3
    print(f"The final result of {y} **= 3 is:", x)
    y=x; x &= 2
    print(f"The final result of {y} &= 2 is:", x)
    y=x; x |= 1
    print(f"The final result of {y} |= 1 is:", x)
    y=x; x ^= 2
    print(f"The final result of {y} ^= 2 is:", x)
    y=x; x >>= 1
    print(f"The final result of {y} >>= 1 is:", x)
    y=x; x <<= 2
    print(f"The final result of {y} <<= 2 is:", x)
    x = 10
    print(f"The final result of 10 := 15 is:", (b := x + 5))


def comparison_operators():
    import random
    x = random.randrange(0,100,5)
    y = random.randrange(0,100,5)
    print("Comparison Operations in Python")
    print("Are the values",x,"and",y,"equal:",x==y)
    print("Are the values",x,"and",y,"different:",x!=y)
    print("Is",x,"greater than",y,":",x>y)
    print("Is",x,"less than",y,":",x<y)
    print("Is",x,"greater than or equal to",y,":",x>=y)
    print("Is",x,"less than or equal to",y,":",x<=y)

def logical_operators():
    import random
    x = random.randrange(0,100,5)
    y = random.randrange(0,100,5)
    z = random.randrange(0,100,5)
    print("Logical Operations in Python")
    print("Is",x,">",z,"and",y,"<",z,":",x>z and y<z)
    print("Is",x,">",z,"or",y,"<",z,":",x>z or y<z)
    print("Is",x,">",z,"not",y,"<",z,":",not (x>z and y<z))

arithmetic_operators()
print("")
assignment_operators()
print("")
comparison_operators()
print("")
logical_operators()