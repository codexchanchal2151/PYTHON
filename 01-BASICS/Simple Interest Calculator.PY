# Program to calculate Simple Interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time period (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"The Simple Interest is: {simple_interest}")
