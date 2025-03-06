from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        l = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            i += 1
        return nums

sol = Solution()
nums = [1, 2, 2, 3, 4, 4]
print(sol.applyOperations(nums))