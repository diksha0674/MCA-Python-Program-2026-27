# Q5. Dictionaries, comprehension and nested collections

employees = {
    101: {"name": "Amit", "department": "IT", "salary": 45000},
    102: {"name": "Neha", "department": "HR", "salary": 35000},
    103: {"name": "Ravi", "department": "Sales", "salary": 50000}
}

print("Original employee records:", employees)

# Add a new employee
employees[104] = {"name": "Sara", "department": "Finance", "salary": 60000}

# Update an employee's salary
employees[102]["salary"] = 38000

# Display keys, values and key-value pairs
print("\nEmployee IDs:", employees.keys())
print("Employee records:", employees.values())
print("All key-value pairs:")
for emp_id, details in employees.items():
    print(emp_id, ":", details)

search_id = int(input("\nEnter employee ID to search: "))
if search_id in employees:
    print("Employee found:", employees[search_id])
else:
    print("Employee not found.")

limit = float(input("Enter salary limit: "))
high_salary = {
    emp_id: details for emp_id, details in employees.items()
    if details["salary"] > limit
}
print("Employees earning above", limit, ":", high_salary)

delete_id = int(input("Enter employee ID to delete: "))
if delete_id in employees:
    del employees[delete_id]
    print("Employee deleted.")
else:
    print("Employee ID not found.")

print("Final employee records:", employees)
