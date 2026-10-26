def rotate_list(lst, k, direction="right"):
    if not lst:
        return lst
    
    # Handle cases where k is greater than the length of the list
    k = k % len(lst)
    
    if direction == "right":
        return lst[-k:] + lst[:-k]
    elif direction == "left":
        return lst[k:] + lst[:k]
    else:
        return "Invalid direction!"

# Example Usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(f"Original List: {my_list}")
    
    k = 2
    print(f"Rotated Right by {k}: {rotate_list(my_list, k, 'right')}")
    print(f"Rotated Left by {k}: {rotate_list(my_list, k, 'left')}")
