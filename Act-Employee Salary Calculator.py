def calculate_salary(name, hours_worked, hourly_rate=15, allowance=0):

    if int(hours_worked) < 0:
        print("Error: Invalid working hours.")
        return

    if hourly_rate < 15:
        print("Error: Minimum hourly rate is RM 15")
        return

    if hours_worked > 40:
        bonus = 100
    else:
        bonus = 0

    basicSalary = hours_worked * hourly_rate
    totalSalary = basicSalary + allowance + bonus

    print("Employee Name: ", name)
    print("Hours Worked: ", hours_worked)
    print("Hourly Rate: RM ", hourly_rate)
    print("Allowance: RM ", allowance)
    print("Bonus: RM ", bonus)
    print("Total Salary: RM ", totalSalary)
    print()

calculate_salary("Alice", 35)
calculate_salary("John", 45, 20)
calculate_salary("Sarah", 50, 25, 300)
