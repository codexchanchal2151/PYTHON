def max_subarray_sum(nums: list[int]) -> tuple[int, list[int]]:
    """
    Finds the contiguous subarray with the largest sum using Kadane's Algorithm.
    Returns (max_sum, subarray).
    """
    if not nums:
        raise ValueError("List cannot be empty")

    current_sum = nums[0]
    max_sum = nums[0]

    start = 0
    temp_start = 0
    end = 0

    for i in range(1, len(nums)):
        # Agar pichla sum negative ho chuka hai, toh naye element se fresh start behtar hai
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start : end + 1]


if __name__ == "__main__":
    sample_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    total, subarray = max_subarray_sum(sample_list)
    print(f"Input List: {sample_list}")
    print(f"Maximum Subarray Sum: {total}")
    print(f"Subarray: {subarray}")
