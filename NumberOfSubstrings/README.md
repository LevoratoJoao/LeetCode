# 1358. Number of Substrings Containing All Three Characters

## Sliding Window

This problem is very similar to [3306. Count of Substrings Containing Every Vowel and K Consonants II](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/).

We use a Sliding Window and a HashMap to keep track of the characters in the current window (using an array of size 3 for the characters 'a', 'b', 'c' is slightly faster than a HashMap).

When we have all three characters in the window, we can perform a calculation to count the number of substrings that can be formed, this calculation is the length of the string minus the position of the right pointer, that will give us the total number of substrings that can be formed with the current window.

After that, we decrease the count of the character at the left pointer and move the left pointer to the right.

```python
def numberOfSubstrings(s: str) -> int:
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
```

Using array:

```python
def numberOfSubstrings(s: str) -> int:
    left = 0
    abcCount = [0] * 3
    count = 0
    for right in range(len(s)):
        abcCount[ord(s[right]) - ord('a')] += 1
        while abcCount[0] > 0 and abcCount[1] > 0 and abcCount[2] > 0:
            count += len(s) - right
            abcCount[ord(s[left]) - ord('a')] -= 1
            left += 1
    return count
```