from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        left = 0
        countS, countP = defaultdict(int), defaultdict(int)
        right = len(p)
        ans = []
        for c in range(len(p)):
            countS[s[c]] += 1
            countP[p[c]] += 1
        if countS == countP: ans = [0]
        else: ans = []

        for right in range(len(p), len(s)):
            countS[s[right]] += 1
            countS[s[left]]  -= 1
            if countS[s[left]] == 0:
                countS.pop(s[left])
            left += 1
            if countS == countP:
                ans.append(left)
        return ans

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc")) # [0, 6]