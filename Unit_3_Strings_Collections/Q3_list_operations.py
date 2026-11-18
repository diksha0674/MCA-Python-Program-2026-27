# Q3. List operations and list comprehension

n = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(n):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

print("Original list:", numbers)

position = int(input("Enter position to insert (0-based index): "))
new_value = int(input("Enter value to insert: "))
if 0 <= position <= len(numbers):
    numbers.insert(position, new_value)
else:
    print("Invalid position.")

remove_value = int(input("Enter value to remove: "))
if remove_value in numbers:
    numbers.remove(remove_value)
else:
    print("Value not found.")

print("Current list:", numbers)
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))
else:
    print("The list is empty.")

print("Concatenation:", numbers + [100, 200])
print("Repetition:", numbers * 2)
if numbers:
    print("First element by indexing:", numbers[0])
    print("Membership of 10:", 10 in numbers)

print("Even numbers:", [x for x in numbers if x % 2 == 0])
print("Odd numbers:", [x for x in numbers if x % 2 != 0])
print("Squares:", [x * x for x in numbers])

# Demonstrating list methods
numbers.append(50)
numbers.extend([60, 70])
numbers.insert(0, 5)
print("After append, extend and insert:", numbers)
if numbers:
    removed = numbers.pop()
    print("Popped element:", removed)
numbers.sort()
print("After sort:", numbers)
numbers.reverse()
print("After reverse:", numbers)
