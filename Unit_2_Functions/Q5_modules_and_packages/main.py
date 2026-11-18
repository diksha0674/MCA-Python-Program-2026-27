# Q5. Importing a user-defined module and package
# Run this file from inside the Q5_modules_and_packages folder.

import arithmetic
from arithmetic import add, multiply
from student import show_details, show_result

print("Using complete arithmetic module:")
print("Subtraction:", arithmetic.subtract(20, 5))
print("Division:", arithmetic.divide(20, 5))

print("\nUsing selected imported functions:")
print("Addition:", add(10, 5))
print("Multiplication:", multiply(10, 5))

show_details("Aarav", 101, "MCA")
show_result(450, 500)
