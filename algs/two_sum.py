"""
return index of numbers that add up to target
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums and i != nums.index(diff):  # index --> O(n) linear search
            return [i, nums.index(diff)]
    return None


if __name__ == '__main__':
    print(two_sum([1, 3, 4, 5, 6, 9], 8))
