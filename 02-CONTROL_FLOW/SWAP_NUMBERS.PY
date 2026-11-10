# Program to swap two numbers without using a third variable

num1 = float(input("Enter first number (num1): "))
num2 = float(input("Enter second number (num2): "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping logic
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping: num1 = {num1}, num2 = {num2}")
