import random

class NotEvenError(Exception):
    """Custom exception for non-even numbers."""
    pass

def check_positive_even_number(number):
    print(f"Checking number: {number}")
    try:
        assert number > 0, "AssertionError: The number must be positive!"
        
        if number % 2 != 0:
            raise NotEvenError("CustomError: The number is not even!")
        
    except AssertionError as ae:
        print(ae)
    except NotEvenError as ne:
        print(ne)
    else:
        print(f"The number {number} is positive and even.")
    finally:
        print("End of function execution, cleaning up if necessary.")

print("Test 1: Positive Even Number")
check_positive_even_number(random.randrange(0, 100, 2))

print("\nTest 2: Positive Odd Number")
check_positive_even_number(random.randrange(1, 100, 2))

print("\nTest 3: Negative Even Number")
check_positive_even_number(random.randrange(-100, 0, 2))

print("\nTest 4: Negative Odd Number")
check_positive_even_number(random.randrange(-99, 0, 2))