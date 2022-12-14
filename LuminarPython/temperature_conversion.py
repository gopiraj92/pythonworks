# Temperature conversion

# From Celcius to Farenheit
# From Farenheit to Celcius


print("1. Convert temperature from Celcius to Farenheit")
print("2. Convert temperature from Farenheit to Celcius")

n = int(input("Enter your choice = "))

if(n==1):
    c = int(input("Enter the temperature in Celcius = "))
    tempF = (9/5) * c + 32
    print("The temperature in Farenheit is = ", round(tempF, 2))
elif(n==2):
    f = int(input("Enter the temperature in Farenheit = "))
    tempC = (f-32) * 5/9
    print("The temperature in Celcius is = ", round(tempC, 2))
else:
    print("Invalid choice")
