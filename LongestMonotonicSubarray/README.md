# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

For a good solution, we will use two variables to store the length of the increasing and decreasing subarray ending at the current index we are iterating, we will also use a variable to store the maximum length of the subarray we have seen so far.

In our loop we will have three cases:
1. If the current element is greater than the next element, we will increment the decreasing subarray length and reset the increasing subarray length to 1.
2. If the current element is less than the next element, we will increment the increasing subarray length and reset the decreasing subarray length to 1.
3. If the current element is equal to the next element, we will reset both the increasing and decreasing subarray length to 1.

At each iteration, we will update the maximum length of the subarray we have seen so far using the maximum of the current maximum length and the maximum of the increasing and decreasing subarray length.

The time complexity of this solution is O(n) where n is the length of the input array.

The space complexity of this solution is O(1).

```python
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
```

Java Code:
```java
class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int max_length = 1;
        int inc = 1;
        int dec = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                dec += 1;
                inc = 1;
            } else if (nums[i] < nums[i + 1]) {
                inc += 1;
                dec = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            max_length = Math.max(max_length, Math.max(inc, dec));
        }

        return max_length;
    }
}
```

JavaScript Code:
```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    let inc = 1;
    let dec = 1;
    let max_length = 1;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            dec += 1;
            inc = 1;
        } else if (nums[i] < nums[i + 1]) {
            inc += 1;
            dec += 1;
        } else {
            inc = 1;
            dec = 1;
        }
        max_length = Math.max(max_length, inc, dec);
    }
    return max_length
};
```