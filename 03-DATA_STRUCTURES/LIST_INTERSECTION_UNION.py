def list_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    # Union: All unique elements from both lists
    union_result = list(set1 | set2)
    
    # Intersection: Elements common to both lists
    intersection_result = list(set1 & set2)
    
    # Difference: Elements in list1 that are not in list2
    difference_result = list(set1 - set2)
    
    return union_result, intersection_result, difference_result

# Example Usage:
if __name__ == "__main__":
    l1 = [10, 20, 30, 40, 50]
    l2 = [30, 40, 50, 60, 70]
    
    union, intersection, difference = list_operations(l1, l2)
    
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference (l1 - l2): {difference}")
