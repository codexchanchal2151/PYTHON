def find_maximum(a, b, c):
    """Function to find the maximum of three numbers."""
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

# Example usage:
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    print(f"The largest number is: {find_maximum(num1, num2, num3)}")
