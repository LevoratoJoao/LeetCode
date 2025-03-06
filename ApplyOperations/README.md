# 2460. Apply Operations to an Array

## Brute Force

We simply iterate through the array and apply the operations as described in the problem statement. After that, we create a new array adding the non-zero elements first and then loop through the length of this current array to the length of the original array, adding zeros to the end.
Memory complexity is O(n) and time complexity is O(n).

```python
def applyOperations(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
    res = []
    for i in nums:
        if i != 0:
            res.append(i)
    while len(res) < len(nums):
        res.append(0)
    return res
```

## Optimized

We can optimize the above solution by using a pointer to keep track of the last non-zero element in the array. We iterate through the array and apply the operations as described in the problem statement. After that, we use two pointers, one to keep track of the last non-zero element and the other to loop through the array, we perform a swap operation between the two pointers if the current element is non-zero, if we find a zero, we skip it. Memory complexity is O(1) and time complexity is O(n).

```python
def applyOperations(nums: List[int]) -> List[int]:
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
```