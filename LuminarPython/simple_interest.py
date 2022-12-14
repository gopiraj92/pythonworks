# Find simple interest

# simple interest = (PNR)/100   P = Principal amount, N = number of year/Tenure, R = rate of interest

p = int(input("Enter the Principal amount ="))
n = int(input("Enter the tenure ="))
r = float(input("Enter the rate of interest ="))

si = (p * n * r) / 100

print("The simple interest is =", si)
