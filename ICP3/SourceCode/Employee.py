class Employee:
    totalInstances = 0
    avgSalary = []

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.totalInstances += 1
        Employee.avgSalary.append(salary)

    def getInfo(self):
        print(self.name,
              self.family,
              self.salary,
              self.department)


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        self.fullTime = True
        Employee.__init__(self, name, family, salary, department)

    def getInfo(self):
        print(self.name,
              self.family,
              self.salary,
              self.department,
              "fulltime?", self.fullTime)


def avg(lst):
    return sum(lst) / len(lst)


def main():
    employee1 = Employee("Alhazmi", "Rasheed", 120000, "IT")
    employee1.getInfo()
    employee2 = FullTimeEmployee("Ross", "Geller", 80000, "HR")
    employee2.getInfo()
    print(employee2.__class__.totalInstances)
    print(int(avg(Employee.avgSalary)))


if __name__ == "__main__":
    main()
