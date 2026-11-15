# Program to find the second most frequent element in a list

def second_most_frequent(arr):
    if not arr or len(set(arr)) < 2:
        return "Not enough unique elements"
    
    # Count frequencies using a dictionary
    freq_dict = {}
    for item in arr:
        freq_dict[item] = freq_dict.get(item, 0) + 1
        
    # Sort elements based on frequency in descending order
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_items[1][0]

# Example usage:
if __name__ == "__main__":
    elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    print("List:", elements)
    
    result = second_most_frequent(elements)
    print("Second Most Frequent Element:", result)
