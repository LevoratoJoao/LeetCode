# 49. Group Anagrams

## Hash Table

For this problem, we can use a hash table that maps the count of each character in a word to a list of words that have the same character count.
For example:

- eat: 1 'e', 1 'a', 1 't'
- tea: 1 't', 1 'e', 1 'a'
- ate: 1 'a', 1 't', 1 'e'
```python
HashMap: {
    (1 'e', 1 'a', 1 't'): ['eat', 'tea', 'ate']
}
```

They all have the same character count, so they are anagrams of each other. We loop over all words and the count list represent the quantity of each character in the word and each index represents the letter of the alphabet in order. Then we loop over each character and get the respective index in the count list by subtracting the ordinary value of the current character by the ordinary value of 'a', e.g. a = 80, b = 81, b - a = index 1. After that, we append the word to the hash table and its key is the count list but we need to convert it to a tuple because lists are not hashable in Python. Finally, we return the values of the hash table.

```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    if len(strs) == 1:
        return [strs]

    hash_words = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            # ord('b') - ord('a') = 1 e.g: a=80 and b = 81
            count[ord(c) - ord('a')] += 1

        # Convert count to a tuple since a list can not be a key
        hash_words[tuple(count)].append(s)

    return list(hash_words.values())
```

The time complexity is O(n * m) where n is the number of words and m is the length of the longest word. The space complexity is O(m) because we are storing all words in the hash table.

Java code:
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) {
            return new ArrayList<>();
        }
        if (strs.length == 1) {
            return List.of(List.of(strs[0]));
        }

        Map<String, List<String>> hashWords = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];

            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            String key = Arrays.toString(count);

            if (!hashWords.containsKey(key)) {
                hashWords.put(key, new ArrayList<>());
            }

            hashWords.get(key).add(s);
        }

        return new ArrayList<>(hashWords.values());
    }
}
```


