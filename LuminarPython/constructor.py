# Constructors - used to initialize data members.

# in Python - " __init__ " is the constructor used.
# it is a member function
# used to assign values to ata members
# constructor automatically invoke when an object is created. no need to call that separately

class Rectangle:
    def __init__(self, l, b):              # Constructor
        self.length = l
        self.breadth = b
    def dispdata(self):
        print("Length of rectangle is = ", self.length)
        print("Breadth of rectangle is = ", self.breadth)
        # print("The area of rectangle is = ", self.length * self.breadth)
    def area(self):
        a = self.length * self.breadth
        print("Area of rectangle is = ", a)

r1 = Rectangle(10,5)
r1.dispdata()
r1.area()
print("")
r2 = Rectangle(20, 10)
r2.dispdata()
r2.area()

