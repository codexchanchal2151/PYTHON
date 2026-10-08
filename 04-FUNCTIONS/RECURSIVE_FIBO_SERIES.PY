# Recursive function to find the nth Fibonacci number

def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main program
term = int(input("Enter the term number for Fibonacci series: "))
print(f"The {term}th term of Fibonacci series is: {fibonacci(term)}")
