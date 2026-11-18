# Q2. File handling: write, read and append

filename = "student.txt"

# Write mode creates a file or replaces its previous contents.
file = open(filename, "w")
name = input("Enter student name: ")
roll = input("Enter roll number: ")
file.write("Student Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.close()

# Read complete file
file = open(filename, "r")
print("\nComplete file contents:")
print(file.read())
file.close()

# Append mode adds data without deleting existing contents.
file = open(filename, "a")
extra_name = input("Enter another student name to append: ")
extra_roll = input("Enter roll number: ")
file.write("\nStudent Name: " + extra_name + "\n")
file.write("Roll Number: " + extra_roll + "\n")
file.close()

# Read line by line
file = open(filename, "r")
print("\nFile contents line by line:")
for line in file:
    print(line, end="")
file.close()
