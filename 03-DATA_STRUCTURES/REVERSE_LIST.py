# Program to reverse a list in-place

def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage:
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    print("Original List:", my_list)
    
    reversed_arr = reverse_list(my_list)
    print("Reversed List:", reversed_arr)v
