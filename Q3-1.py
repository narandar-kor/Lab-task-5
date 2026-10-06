Employees = []

for i in range(3):
    name = input(f"\nEnter {i+1} employee name : ")
    Age = int(input("Enter their age : "))
    salary = float(input("Enter their salary : "))

    information = (name,Age,salary)
    Employees.append(information)


print(Employees)