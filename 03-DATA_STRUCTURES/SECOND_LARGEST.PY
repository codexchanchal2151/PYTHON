def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements"
    
    # Remove duplicates and sort the list in descending order
    unique_numbers = sorted(list(set(numbers)), reverse=True)
    
    if len(unique_numbers) < 2:
        return "No second largest element (all elements are same)"
        
    return unique_numbers[1]

if __name__ == "__main__":
    nums = [45, 12, 89, 56, 89, 23, 78]
    print("List:", nums)
    
    second_max = find_second_largest(nums)
    print("Second Largest Number:", second_max)
