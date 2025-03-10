# 3208. Alternating Groups II

## Sliding Window

For this problem we use two techniques:

1. Sliding Window
2. Circular Queue

We start by using a sliding window from 1 to `N + k - 1` where `N` is the length of the array and `k` is the maximum length of the alternating group. This way we can cover all possible alternating groups since the only two more colors that we would need to consider are the ones at the beginning (first one and the second one), we dont need to loop over the entire array again in every window because we already did that in the first window.

Then we check if the color at position `right % N` is the same as the color at position `(right - 1) % N` (the current color is the same as the previous one), if it is, we move the left become the right pointer
the modulo is used to wrap around the array since we are using a circular queue. e.g. if N = 5 and we are at index 6, then `6 % 5 = 1` and `(6 - 1) % 5 = 0` so we are checking if the color at index 6 is the same as the color at index 0.

To keep the window valid, we check `right - left + 1 > k` and if it is, we move the left pointer to the right.
Let's say we have the following array: `[0, 1, 0, 1, 0]` and `k = 3`. When we are at index 3 and left at index 0, we have a window of size 4, so we move the left pointer to the right and now we have a window of size 3.

If the window is valid, we check if `right - left + 1 == k` and if it is, we increment the count. That means that the right pointer is at the last position of the window and we have a valid alternating group

```python
def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
    left = 0
    N = len(colors)
    count = 0
    for right in range(1, N + k - 1):
        if colors[right % N] == colors[(right - 1) % N]:
            left = right
        if right - left + 1 > k:
            left += 1
        if right - left + 1 == k:
            count += 1
    return count
```

