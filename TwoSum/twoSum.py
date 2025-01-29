
def twoSum_brute(nums, target):
    seen = {}
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] < target:
            seen[nums[i] + nums[j]] = (i, j)
        if target in seen:
            return [i, j]
        i+=1
        j+=1
    return seen.get(target)

twoSum_brute([3,2,3], 6)