# Q3. File methods and exception handling

filename = input("Enter name of an existing text file: ")

try:
    file = open(filename, "r")
    print("File name:", file.name)
    print("File mode:", file.mode)

    print("\nUsing read():")
    print(file.read())

    print("Current position after read():", file.tell())

    file.seek(0)
    print("\nUsing readline():")
    print(file.readline())

    file.seek(0)
    print("\nUsing readlines():")
    print(file.readlines())

    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
else:
    print("File operations completed successfully.")
finally:
    print("File handling process finished.")
