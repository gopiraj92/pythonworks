# Grade of a student.
 # Enter the marks of 3 subjects out of 100
 # find average mark (Total mark/300)*100
 # if average mark is >= 80 give grade A, 79-60 grade B, 59-50 grade C, 49-40 grade D, below 40 Failed

sub1 = int(input("Enter the mark of subject 1 = "))
sub2 = int(input("Enter the mark of subject 2 = "))
sub3 = int(input("Enter the mark of subject 3 = "))

if (sub1<=100 and sub2<=100 and sub3<=100):
    tm = sub1 + sub2 + sub3

    avg = (tm/300)*100

    print("The average mark of student is = ", avg)

    if avg >= 80:
        print("The grade of student is A")
    elif (avg < 80 and avg >= 60):
        print("The grade of student is B")
    elif (avg < 60 and avg >= 50):
        print("The grade of student is C")
    elif (avg < 50 and avg >= 40):
        print("The grade of student is D")
    else:
     print("Failed")

else:
    print("Wrong mark entry...!")

