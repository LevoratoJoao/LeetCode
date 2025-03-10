class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
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

solution = Solution()
print(solution.minimumRecolors("WBBWWBBWBW", 7))