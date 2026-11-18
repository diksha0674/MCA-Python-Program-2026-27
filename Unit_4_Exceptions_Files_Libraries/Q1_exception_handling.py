# Q1. Exception handling

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print("Division result:", result)
finally:
    print("Division operation completed.")

try:
    values = [10, 20, 30]
    index = int(input("\nEnter list index (0 to 2): "))
    print("Selected value:", values[index])
except ValueError:
    print("Error: Index must be an integer.")
except IndexError:
    print("Error: List index is out of range.")
finally:
    print("List operation completed.")

try:
    age = int(input("\nEnter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
except ValueError as error:
    print("Age error:", error)
else:
    print("Age accepted.")
finally:
    print("Age verification completed.")
