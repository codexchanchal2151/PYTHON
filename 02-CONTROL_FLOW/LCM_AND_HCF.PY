# Program to find LCM and HCF (GCD) of two numbers

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

# Finding HCF using Euclidean algorithm
a, b = num1, num2
while b != 0:
    a, b = b, a % b

hcf = a

# Finding LCM using the formula: (num1 * num2) / HCF
lcm = (num1 * num2) // hcf

print(f"The HCF (GCD) of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")
