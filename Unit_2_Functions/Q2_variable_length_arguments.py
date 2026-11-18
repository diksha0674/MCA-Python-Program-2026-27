# Q2. *args, **kwargs and return statement

def student_result(name, *marks, **details):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    highest = max(marks) if marks else 0

    print("\nStudent Name:", name)
    for key, value in details.items():
        print(key.title() + ":", value)

    return total, average, highest

name = input("Enter student name: ")
roll = input("Enter roll number: ")
student_class = input("Enter class: ")

count = int(input("Enter number of subjects: "))
marks = []
for i in range(count):
    marks.append(float(input(f"Enter marks for subject {i + 1}: ")))

total, average, highest = student_result(
    name, *marks, roll_number=roll, class_name=student_class
)

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
