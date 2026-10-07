# Program to swap two numbers using a temporary variable

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping using temporary variable
temp = num1
num1 = num2
num2 = temp

print(f"After swapping: num1 = {num1}, num2 = {num2}")
