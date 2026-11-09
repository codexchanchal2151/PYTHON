def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

# Example usage:
if __name__ == "__main__":
    n = 5  # Numbers from 1 to 5
    numbers = [1, 2, 4, 5]  # 3 is missing
    missing = find_missing_number(numbers, n)
    print(f"The missing number is: {missing}")
