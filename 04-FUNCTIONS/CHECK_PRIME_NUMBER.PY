def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example Usage
num = int(input("Enter a number to check prime: "))
if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")
