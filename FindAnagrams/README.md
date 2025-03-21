# 438. Find All Anagrams in a String

For this problem I recommend doing the [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) problem first if you haven't already. This problem is a bit more difficult than that one but follows the same pattern, we have a guide for that problem [here](../ValidAnagram/README.md).

## Sliding Window and Hash Table

We start this problem looping through the string length of `s` and adding the characters to a hash table of `s` and `p`. Thats the initial case, where our window is the size of `p`, we then compare the hash tables and if they are equal we add the index `0` to our result list.

After that we start the slinding window process, going through the `len(p)` to `len(s)`, we add every new character to our hash table of `s` (our right pointer) and decrease the counter of the character that is no longer in our window (our left pointer), if this counter reaches `0` we remove the character from the hash table.

At the end of the loop we compare the hash tables and if they are equal we add the index of the left pointer to our result list.

```python
def findAnagrams(s: str, p: str) -> List[int]:
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
```
