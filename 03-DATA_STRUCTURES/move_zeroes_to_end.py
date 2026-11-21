def move_zeroes_to_end(nums):
    insert_pos = 0

    # Non-zero elements ko aage shift karo
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Baaki bachi jagah par zeroes bharo
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums


if __name__ == "__main__":
    raw = input("Enter numbers separated by space: ").strip()
    arr = list(map(int, raw.split())) if raw else []
    print("Updated list:", move_zeroes_to_end(arr))
