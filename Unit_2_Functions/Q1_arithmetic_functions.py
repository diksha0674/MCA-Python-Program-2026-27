# Q1. Arithmetic operations using user-defined functions

def add(a, b, operation="addition"):
    return a + b

def subtract(a, b, operation="subtraction"):
    return a - b

def multiply(a, b, operation="multiplication"):
    return a * b

def divide(a, b, operation="division"):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Positional arguments
print("Addition:", add(num1, num2))

# Keyword arguments
print("Subtraction:", subtract(a=num1, b=num2))
print("Multiplication:", multiply(a=num1, b=num2))
print("Division:", divide(a=num1, b=num2))
