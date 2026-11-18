# Q4. Python standard libraries

import math
import random
from datetime import datetime, date

number = float(input("Enter a positive number: "))
print("\nMATH LIBRARY")
print("Square root:", math.sqrt(number))
print("Factorial (integer input):", math.factorial(int(number)))
print("Power (number raised to 2):", math.pow(number, 2))
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))

print("\nRANDOM LIBRARY")
print("Random integer from 1 to 100:", random.randint(1, 100))
items = ["Apple", "Banana", "Mango", "Orange"]
print("Random item:", random.choice(items))
random.shuffle(items)
print("Shuffled list:", items)

print("\nDATETIME LIBRARY")
now = datetime.now()
print("Current date and time:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)

date1 = date(2026, 1, 1)
date2 = date.today()
difference = date2 - date1
print("Difference between", date1, "and", date2, ":", difference.days, "days")
