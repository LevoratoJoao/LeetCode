# 290. Word Pattern

## One Hash Map

For this solution we will use one hash map to store the mapping between the words with the characters, e.g. `a -> dog`, `b -> cat`, `c -> fish`, etc.
First we check if the length of the pattern is equal to the length of the words splited by space. If not, we return False.
Then we iterate through the words (or each character in the pattern) and check if the word is in the hash map AND if the word is in the values of the hash map (we could also swap the keys and values and check if the character is in the keys of the hash map). If not, we add the word and the character to the hash map. If the word is in the hash map, we check if the character is equal to the value of the hash map. If not, we return False.

```python
def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words): return False

    hashMap = defaultdict(str)

    for i, word in enumerate(words):
        if word not in hashMap and pattern[i] not in hashMap.values():
            hashMap[word] = pattern[i]
        else:
            if hashMap[word] != pattern[i]: return False
    return True
```

The time complexity is O(n) and the space complexity is O(n), where n is the length of the pattern or the number of words in the string s.

## Two Hash Maps

We could also use two hash maps to store the mapping between the words with the characters and the mapping between the characters with the words. The implementation is similar to the previous solution.

```python
def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words): return False

    hashMap1 = defaultdict(str)
    hashMap2 = defaultdict(str)

    for i, word in enumerate(words):
        if word not in hashMap1 and pattern[i] not in hashMap2:
            hashMap1[word] = pattern[i]
            hashMap2[pattern[i]] = word
        else:
            if hashMap1[word] != pattern[i] or hashMap2[pattern[i]] != word: return False
    return True
```
