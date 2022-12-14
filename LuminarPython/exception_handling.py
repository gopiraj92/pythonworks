# Exception handling

# a = int(input("Enter first number = "))
# b = int(input("Enter second number = "))
#
# try:                # Suspected code
#     div = a/b
#     print(div)
# except:             # Code for handling exception
#     print("Not enter 0 as second number")


try:
    a = int(input("Enter the first number ="))
    b = int(input("Enter the second number ="))
    c = a/b
    print(c)

# except ValueError:
#     print("You must enter a number")
# except ZeroDivisionError:
#     print("Enter the second number other than zero")
except:
    print("All other errors handle error")
# else:
#     print("Execute if there is no errors")
finally:
    print("Always execute")