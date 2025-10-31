salary = float(input("Enter  salary:"))

if salary < 0:
    raise ValueError("Salary cannot be negative")
else:
    print(f"your salary is {salary}")