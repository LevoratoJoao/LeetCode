from typing import List

def longestMonotonicSubarray(nums: List[int]) -> int:
    inc = 1
    dec = 1
    max_length = 1
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            dec += 1
            inc = 1
        elif nums[i] < nums[i + 1]:
            inc += 1
            dec = 1
        else:
            inc = dec = 1
        max_length = max(max_length, inc, dec)
    return max_length

print(longestMonotonicSubarray([1,4,3,3,2]
))