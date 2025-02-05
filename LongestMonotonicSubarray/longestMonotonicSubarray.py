from typing import List


def longestMonotonicSubarray(nums: List[int]) -> int:
    inc = set()
    dec = set()
    for i in range(0, len(nums)):
        if i + 1 < len(nums) and nums[i] < nums[i + 1]:
            inc.add(nums[i])
            inc.add(nums[i + 1])
        if i + 1 < len(nums) and nums[i + 1] < nums[i]:
            dec.add(nums[i])
            dec.add(nums[i + 1])
    if len(inc) > len(dec):
        return len(inc)
    return len(dec)

print(longestMonotonicSubarray([1,4,3,3,2]
))