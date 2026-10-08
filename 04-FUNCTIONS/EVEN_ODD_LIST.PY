# Function to count even and odd numbers in a list

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Main program
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens, odds = count_even_odd(nums)

print(f"Given list: {nums}")
print(f"Total Even numbers: {evens}")
print(f"Total Odd numbers: {odds}")
