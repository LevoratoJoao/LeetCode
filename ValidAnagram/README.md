# 242. Valid Anagram

## Hash Table solution

We can use a hash table to count the frequency of each letter in the input strings. If the frequency of each letter is the same for both strings, then the strings are anagrams of each other.

```python
def isAnagram(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    hash_s, hash_t = defaultdict(int), defaultdict(int)
    for i in range(len(s)):
        hash_s[s[i]] += 1
        hash_t[t[i]] += 1
    for i in hash_s:
        t_value = hash_t[i]
        s_value = hash_s[i]
        if t_value != s_value :
            return False
    return True
```

Other approache would be to subtract the frequency of each letter in the second string from the frequency of each letter in the first string. If the frequency of each letter is zero for both strings, then the strings are anagrams of each other.

```python
def isAnagram(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    hash_s = defaultdict(int)
    for i in s:
        hash_s[i] += 1
    for i in t:
        hash_s[i] -= 1
    for i in hash_s:
        s_value = hash_s[i]
        if s_value != 0:
            return False
    return True
```

## Sorting solution

Another approach is to sort the strings and compare them. If the strings are anagrams of each other, then after sorting, the strings will be the same.
But this solution relies on the built-in sorting function, which may not be allowed in the problem statement.