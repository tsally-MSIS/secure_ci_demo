# Testing 1 
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("You cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print("Addition of 4 and 4 is:", add(4, 4))
    print("Subtraction of 6 from 10 is:", subtract(10, 6))
    print("Multiplication of 6 and 6 is:", multiply(6, 6))
    print("Division of 10 by 5 is:", divide(10, 5))

print("Please try again..!")