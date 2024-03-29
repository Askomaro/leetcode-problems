#
# Given an array with n integers, your task is to check if it could become non-decreasing
# by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:
# Input: [4,2,1]
# Output: False

# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].


def approach1(nums):
    p = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if p is not None:
                return False
            p = i

    return (p is None or p == 0 or p == len(nums) - 2 or
            nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2])


if __name__ == '__main__':
    # delta is -2, 1
    assert approach1([4, 2, 3]) is True
    # delta is 1, -2, 1
    assert approach1([3, 4, 2, 3]) is False
    # delta is 1, 0, -1, 2
    assert approach1([2, 3, 3, 2, 4]) is True
