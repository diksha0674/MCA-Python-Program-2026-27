# Q4. Scope, lifetime and lambda functions

value = 10  # Global variable

def show_scope():
    local_value = 5  # Local variable
    print("Global value inside function:", value)
    print("Local value inside function:", local_value)

def change_global():
    global value
    value = 20
    print("Global value changed inside function:", value)

show_scope()
change_global()
print("Global value outside function:", value)
# local_value exists only while show_scope() is executing.

# Lambda functions
square = lambda x: x * x
cube = lambda x: x * x * x
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("Square of first number:", square(a))
print("Cube of first number:", cube(a))
print("Maximum:", maximum(a, b))
print("Addition:", addition(a, b))
