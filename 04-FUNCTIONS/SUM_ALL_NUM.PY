# Function to find the sum of arbitrary numbers

def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program
print("Sum of (5, 10):", calculate_sum(5, 10))
print("Sum of (1, 2, 3, 4, 5):", calculate_sum(1, 2, 3, 4, 5))
