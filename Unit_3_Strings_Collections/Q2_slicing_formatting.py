# Q2. String slicing and formatting

name = input("Enter full name: ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter mobile number: ").strip()

parts = name.split()
first_name = parts[0] if parts else ""
last_name = parts[-1] if len(parts) > 1 else ""

email_parts = email.split("@")
username = email_parts[0] if len(email_parts) == 2 else "Invalid email"
domain = email_parts[1] if len(email_parts) == 2 else "Invalid email"

print("\nStudent Information")
print(f"Full Name: {name}")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Reversed Name:", name[::-1])
print("Email Username:", username)
print("Email Domain:", domain)
print("Last four mobile digits:", mobile[-4:])
print("Positive indexing (first character):", name[0] if name else "")
print("Negative indexing (last character):", name[-1] if name else "")

print("Using format(): Name: {}, Email: {}".format(name, email))
print("Using % formatting: Name: %s, Mobile: %s" % (name, mobile))
