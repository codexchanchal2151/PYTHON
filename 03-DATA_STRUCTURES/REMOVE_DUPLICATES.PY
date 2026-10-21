def remove_duplicates(input_list):
    # Using set to remove duplicates and converting it back to a list
    unique_list = list(set(input_list))
    return unique_list

if __name__ == "__main__":
    numbers = [10, 20, 20, 30, 40, 10, 50, 30]
    print("Original List:", numbers)
    
    result = remove_duplicates(numbers)
    print("List after removing duplicates:", result)
