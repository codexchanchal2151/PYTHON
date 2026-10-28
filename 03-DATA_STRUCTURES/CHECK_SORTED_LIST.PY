def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

# Example Usage:
if __name__ == "__main__":
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 5, 3, 9]
    
    print(f"List {list1} is sorted? {is_sorted(list1)}")
    print(f"List {list2} is sorted? {is_sorted(list2)}")
