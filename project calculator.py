value1 = float(input("enter your first value: "))
value2 = float(input("enter your second value: "))
sum = value1 + value2
multiplication = value1 * value2
subtraction = value1 - value2
division = value1 / value2
value3 = input("your mathematical operation: ")

if value3.lower() == "sum":
    print("sum: ", str(sum))
elif value3.lower() == "multiplication":
    print("multiplication: ",str(multiplication))
elif value3.lower() == "subtraction":
    print("subtraction: ",str(subtraction))
else:
    print("division: ", str(division))