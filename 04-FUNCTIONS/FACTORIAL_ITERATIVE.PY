def calculate_factorial(n):
    """Function to calculate factorial iteratively."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    print(f"Factorial of {num} is: {calculate_factorial(num)}")
