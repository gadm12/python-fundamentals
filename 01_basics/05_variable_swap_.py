a = input("first value (a): ")
b = input("second value (b): ")
empty_var = 0
print(f"Before swapping a: {a}, b: {b}")

# Method 1: The "Classic" Way

temp = a
a = b
b = temp


print(f"After swapping a: {a}, b: {b}")

# Method 2: The "Pythonic" Way
a, b = b, a

print(f"After Python Swap: a: {a}, b: {b}")
