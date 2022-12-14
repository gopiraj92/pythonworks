# OOPs - Object Oriented Programming

# Eg. 1.

# class Student:
#     def read(self):
#         self.rollno = int(input("Enter the roll number = "))
#         self.name = input("Enter the name = ")
#     def display(self):
#         print("Roll number : ",self.rollno)
#         print("Name : ",self.name)
#
# # objectname = classname()
#
# s1 = Student()
# s1.read()
# s1.display()
# s2 = Student()
# s2.read()
# s2.display()


# Eg. 2.

# class Rectangle:
#     def getdata(self):
#         self.length = int(input("Enter length = "))
#         self.breadth = int(input("Enter breadth = "))
#     def dispdata(self):
#         print("Length of rectangle is = ", self.length)
#         print("Breadth of rectangle is = ", self.breadth)
#         # print("The area of rectangle is = ", self.length * self.breadth)
#     def area(self):
#         a = self.length * self.breadth
#         print("Area of rectangle is = ", a)

# r1 = Rectangle()
# r1.getdata()
# r1.dispdata()
# r1.area()
#
# r2 = Rectangle()
# r2.getdata()
# r2.dispdata()
# r2.area()

# r3 = Rectangle()
# r3.getdata()
# r3.dispdata()
#
# r4 = Rectangle()
# r4.getdata()
# r4.dispdata()


# Eg. 3.

# class Circle:
#     def read(self):
#         self.radius = int(input("Enter the radius of circle = "))
#     def display(self):
#         print("The radius of circle is = ", self.radius)
#     def area(self):
#         a = 3.14 * self.radius * self.radius
#         print("The area of circle is = ", a)
#
# c1 = Circle()
# c1.read()
# c1.display()
# c1.area()
#
# c2 = Circle()
# c2.read()
# c2.display()
# c2.area()


# Eg. 4. Parametric style

class Rectangle:
    def getdata(self, l, b):
        self.length = l          # public data member
        self.__breadth = b       # private data member. to make private, add '__' before variable name. eg __breadth=b
    def dispdata(self):
        print("Length of rectangle is = ", self.length)
        print("Breadth of rectangle is = ", self.__breadth)
        # print("The area of rectangle is = ", self.length * self.breadth)
    def area(self):
        a = self.length * self.__breadth
        print("Area of rectangle is = ", a)

r1 = Rectangle()
r1.getdata(10, 5)
r1.dispdata()
r1.area()
print(r1.length)
print(r1.__breadth)
# r2 = Rectangle()
# r2.getdata(20, 15)
# r2.dispdata()
# r2.area()