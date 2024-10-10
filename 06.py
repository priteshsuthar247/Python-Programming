import random

global_var = random.randrange(1, 100, 5)
def outer_function():
    local_var = random.randrange(1, 100, 5)

    def inner_function():
        nonlocal local_var  
        global global_var    
        local_var = local_var * 10
        global_var = global_var - 10
        print("Inside inner_function, local_var:", local_var)
        print("Inside inner_function, global_var:", global_var)
    
    print("Before inner_function, local_var:", local_var)
    print("Before inner_function, global_var:", global_var)
    inner_function()
    print("After inner_function, local_var:", local_var)

def function_scoping():
    print("Demonstration of scoping.")
    outer_function()
    print("Main function, global_var:", global_var)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def recursion_example():
    print("Demonstartion of recusrion.")
    n = random.randrange(0,10,1)
    print(f"Factorial of {n} is:", factorial(n))

def list_operations():
    print("Demonstarion of list mutability.")
    l1 = [1, 2, 3, 4, 5]
    print(f"Original tuple t1 is: {l1}")
    l2 = l1[1:3]
    print(f"Slicing tuple t1 reults in: {l2}")
    l3 = l1 + l2
    print(f"Concatnating t1 and t2 results in: {l3}")
    l4 = l1 * 2
    print(f"Performing repeatation on t1 results in: {l4}")
    print(f"Is 9 present in tuple t1: {9 in l1}")
    print(f"length of tuple t2 is: {len(l1)}")

function_scoping()
print()
recursion_example()
print()
list_operations()