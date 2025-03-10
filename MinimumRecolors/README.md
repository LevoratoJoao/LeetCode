# 2379. Minimum Recolors to Get K Consecutive Black Blocks

## Sliding Window

For this problem we will just count the number of white blocks in the current window instead of the minimum number of operations needed. The process of doing the right pointer minus the left pointer plus one is a crucial part of the sliding window technique, that way we keep the size of the window constant.


We loop through the blocks and keep track of the number of white blocks in the current window, if the difference between the right and left pointer plus one is equal to k that means our window has reached the end. We now need to update the minimum number of white blocks that need to be recolored and then observe that we dont need to loop through the new window again computing the number of white blocks, we just decrease the count of white blocks if the left pointer is pointing to a white block and increase the left pointer itself and continue the process.

```python
def minimumRecolors( blocks: str, k: int) -> int:
    left = 0
    whiteCount = 0
    minWhiteCount = k
    for right in range(len(blocks)):
        if blocks[right] == 'W':
            whiteCount += 1
        if right - left + 1 == k:
            minWhiteCount = min(minWhiteCount, whiteCount)
            if blocks[left] == 'W':
                whiteCount -= 1
            left += 1
    return minWhiteCount
```