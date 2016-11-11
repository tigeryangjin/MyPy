class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


e1 = Employee('bill', 500)
e2 = Employee('john', 800)

e1.displayEmployee()
e1.displayCount()
e2.displayEmployee()
e2.displayCount()
