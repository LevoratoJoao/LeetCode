from typing import List


class Solution:
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

sol = Solution()
print(sol.numberOfAlternatingGroups([0,1,0,1,0], 3))
