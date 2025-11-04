# help(Exception)

class SalaryError(Exception):
    pass


# raise SalaryError("Invaled salary")

def chaecksalary(salary):
    if salary < 0:
        raise SalaryError("Salary cannot be negative")
    else:
        bonus = 0.1 * salary
        return salary+bonus

salary = int(input("Enter salary: "))
final_salary = chaecksalary(salary)
print(final_salary)


# Transection