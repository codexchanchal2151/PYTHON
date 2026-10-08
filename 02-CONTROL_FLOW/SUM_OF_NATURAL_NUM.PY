# Sum of Natural Numbers

n = int(input("Enter a positive integer: "))

if n < 0:
    print("Please enter a positive integer.")
else:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print(f"The sum of natural numbers up to {n} is: {total_sum}")
