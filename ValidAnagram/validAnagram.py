from collections import defaultdict

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
print(isAnagram("anagram", "nagaram"))

