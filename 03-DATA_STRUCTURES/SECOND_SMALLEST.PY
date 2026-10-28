def find_second_smallest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two elements"
    
    smallest = second_smallest = float('inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
            
    if second_smallest == float('inf'):
        return "No second smallest element found (all elements might be equal)"
    return second_smallest

# Example Usage:
if __name__ == "__main__":
    nums = [12, 45, 2, 41, 31, 10, 2]
    print(f"Original List: {nums}")
    print(f"Second Smallest Number: {find_second_smallest(nums)}")
