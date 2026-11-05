class Employee :
    def __init__(self, name, employee_id, base_salary):
        if base_salary < 0 :
            raise ValueError("Salary cannot be Negative")
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, bonus = 0):
        super().__init__(name, employee_id, base_salary)
        if bonus < 0 :
            raise ValueError("Bonus Cannot be Negative ")
        self.bonus = bonus 

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, allowance = 0):
        if allowance < 0 :
                    raise ValueError("Allowance cannot be Negative")
        super().__init__(name, employee_id, base_salary)
        self.allowance = allowance
    def calculate_salary(self):
        return super().calculate_salary() + self.allowance

    
emp1 = Employee("Amol", 101, 125)

dev = Developer("Ram", 102, 758, 30)

manager = Manager("Sita", 103, 741, 36)

employees = [emp1, dev, manager]
for employee in employees:
    print(employee.name)
    print(employee.employee_id)
    print(employee.calculate_salary())