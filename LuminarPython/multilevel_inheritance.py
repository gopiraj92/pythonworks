# Multilevel Inheritance

# Eg 1.

# class Student:
#     def getdata(self):
#         self.name = input("Enter the name = ")
#         self.rollno = int(input("Enter the roll number = "))
#     def printdata(self):
#         print("Name = ", self.name)
#         print("Roll number = ", self.rollno)
#
# class Mark(Student):
#     def getmark(self):
#         self.mark = int(input("Enter the mark = "))
#     def printmark(self):
#         print("Total marks obtained = ", self.mark)
#
# class Grade(Mark):
#     def calcgrade(self):
#         p = (self.mark/500)*100
#         if(p>=90):
#             print("Grade is = A")
#         elif(p>=80):
#             print("Grade is = B")
#         elif(p>=70):
#             print("Grade is = C")
#         elif(p>=60):
#             print("Grade is = D")
#         elif(p>=50):
#             print("Grade is = E")
#         else:
#             print("Failed...!")
#
#
# obj1 = Grade()
# obj1.getdata()
# obj1.getmark()
# obj1.printdata()
# obj1.printmark()
# obj1.calcgrade()


# Eg 2. Using __init__ (constructor)

# class Student:
#     def __init__(self):
#         self.roll = int(input("Enter the roll number ="))
#         self.name = input("Enter the name = ")
#     def printdata(self):
#         print("Roll number = ", self.roll)
#         print("Name = ", self.name)
#
# class Mark(Student):
#     def __init__(self):
#         Student.__init__(self)
#         self.mark = int(input("Enter the mark = "))
#     def printmark(self):
#         print("Total mark = ", self.mark)
#
# class Grade(Mark):
#     def __init__(self):
#         Mark.__init__(self)
#     def calcgrade(self):
#         p = (self.mark / 500) * 100
#         if (p >= 90):
#             print("Grade is = A")
#         elif (p >= 80):
#             print("Grade is = B")
#         elif (p >= 70):
#             print("Grade is = C")
#         elif (p >= 60):
#             print("Grade is = D")
#         elif (p >= 50):
#             print("Grade is = E")
#         else:
#             print("Failed...!")
#
# obj1 = Grade()
# obj1.printdata()
# obj1.printmark()
# obj1.calcgrade()


# Eg 3. Parametric form

class Student:
    def __init__(self,r,n):
        self.roll = r
        self.name = n
    def printdata(self):
        print("Roll number = ", self.roll)
        print("Name = ", self.name)

class Mark(Student):
    def __init__(self,r,n,m):
        Student.__init__(self,r,n)
        self.mark = m
    def printmark(self):
        print("Total mark = ", self.mark)

class Grade(Mark):
    def __init__(self,r,n,m):
        Mark.__init__(self,r,n,m)
    def calcgrade(self):
        p = (self.mark / 500) * 100
        if (p >= 90):
            print("Grade is = A")
        elif (p >= 80):
            print("Grade is = B")
        elif (p >= 70):
            print("Grade is = C")
        elif (p >= 60):
            print("Grade is = D")
        elif (p >= 50):
            print("Grade is = E")
        else:
            print("Failed...!")

obj1 = Grade(45,'anu',375)
obj1.printdata()
obj1.printmark()
obj1.calcgrade()