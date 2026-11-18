# Q5. Command-line arguments
# Run examples:
# python Q5_command_line_arguments.py 10 5 +
# python Q5_command_line_arguments.py 10 5 *

import sys

if len(sys.argv) != 4:
    print("Usage: python Q5_command_line_arguments.py number1 number2 operator")
    sys.exit()

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operator = sys.argv[3]

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        print("Invalid operator. Use +, -, * or /.")
        sys.exit()

    print("Result:", result)
except ValueError:
    print("Please provide valid numeric arguments.")
except ZeroDivisionError as error:
    print("Error:", error)
