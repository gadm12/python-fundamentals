print("*** Welcome to the simple calculator ***")

num1 = float(input("enter the 1st number: "))
num2 = float(input("enter the 2nd number: "))

# Addition (sum), Subtraction (difference), Multiplication (product), and Division (quotient)
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
