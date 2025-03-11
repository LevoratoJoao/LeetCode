from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        abcCount = defaultdict(int)
        count = 0
        for right in range(len(s)):
            abcCount[s[right]] += 1
            while abcCount['a'] > 0 and abcCount['b'] > 0 and abcCount['c'] > 0:
                count += len(s) - right
                abcCount[s[left]] -= 1
                left += 1
        return count

sol = Solution()
print(sol.numberOfSubstrings("aaacb"))