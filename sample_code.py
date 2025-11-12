# Testing 1 
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print("Addition of 3 and 3 is:", add(3, 3))
    print("Subtraction of 6 from 10 is:", subtract(10, 6))
    print("Multiplication of 5 and 5 is:", multiply(5, 5))
    print("Division of 10 by 3 is:", divide(10, 3))