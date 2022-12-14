# Multiple inheritance

# A -> C <- B  ie, a child class having inherited with the properties from two or more super classes.

class Mark:
    def getmark(self):
        self.m = int(input("Enter the mark = "))
    def printmark(self):
        print("Marks obtained = ", self.m)

class gracemark:
    def getgmark(self):
        self.gm = int(input("Enter Grace mark = "))
    def printgmark(self):
        print("Grace mark = ", self.gm)

class Grade(Mark):
    def calcgrade(self):
        total = self.m + self.gm
        p = (total/500)*100
        if(p>=90):
            print("Grade is = A")
        elif(p>=80):
            print("Grade is = B")
        elif(p>=70):
            print("Grade is = C")
        elif(p>=60):
            print("Grade is = D")
        elif(p>=50):
            print("Grade is = E")
        else:
            print("Failed...!")