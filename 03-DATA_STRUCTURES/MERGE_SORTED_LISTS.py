# Program to merge two sorted lists into a single sorted list

def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Remaining elements add karna
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# Example inputs
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

print("List 1:", l1)
print("List 2:", l2)
print("Merged Sorted List:", merge_sorted_lists(l1, l2))
