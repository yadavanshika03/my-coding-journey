print("**************** CALCULATOR ****************")
print()

num1 = int(input("Enter the first number here:"))
num2 = int(input("Enter the second number here:"))

print("Enter 1 for 'Addition'")
print("Enter 2 for 'Subtraction'") 
print("Enter 3 for 'Multiply'")
print("Enter 4 for 'Division'")

choice = int(input("choice a number from 1 to 4:"))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    print("Result:", num1 / num2)
else:
    print("Galat choice! 1 se 4 ke beech me daalo")