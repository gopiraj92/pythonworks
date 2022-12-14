# Inheritance

 # Parent class/Super class
 # Child class/Derived class

# class Person:             # Parent class/Super class
#     def getdata(self):
#         self.name = input("Enter the name = ")
#         self.vid = input("Enter the voter id = ")
#     def printdata(self):
#         print("The name is = ", self.name)
#         print("The voter id is = ", self.vid)
#
# class Employee(Person):        # Child class/Derived class
#     def getdata(self):
#         super().getdata()
#         self.salary = int(input("Enter the salary = "))
#     def printdata(self):
#         super().printdata()
#         print("The salary is = ", self.salary)
#
# e1 = Employee()
# e1.getdata()
# e1.getsalary()
# e1.printdata()
# e1.printsalary()

# e2 = Employee()
# e2.getdata()
# e2.getsalary()
# e2.printdata()
# e2.printsalary()


# Overriding - if child class have the function name same as in the parent class, the child class funtion override the parent class


# using __init__

# class Person:             # Parent class/Super class
#     def __init__(self):
#         self.name = input("Enter the name = ")
#         self.vid = input("Enter the voter id = ")
#     def printdata(self):
#         print("The name is = ", self.name)
#         print("The voter id is = ", self.vid)
#
# class Employee(Person):        # Child class/Derived class
#     def __init__(self):
#         super().__init__()
#         self.salary = int(input("Enter the salary = "))
#     def printdata(self):
#         super().printdata()
#         print("The salary is = ", self.salary)
#
# e1 = Employee()
# e1.printdata()


# Eg.

class Person:
    def __init__(self,l,b):
        self.vid = l
        self.name = b
    def printdata(self):
        print("Voter ID", self.vid)
        print("Name", self.name)

class Employee(Person):
    def __init__(self,l,b,s):
        super().__init__(l,b)
        self.salary = s
    def printdata(self):
        super().printdata()
        print("Salary", self.salary)

emp1 = Employee(223, 'Appu', 25000)
emp1.printdata()
