def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
        
    print(f"Fibonacci series up to {n} terms: {fib_series}")

# Example Usage:
n_terms = int(input("Enter number of terms: "))
generate_fibonacci(n_terms)
