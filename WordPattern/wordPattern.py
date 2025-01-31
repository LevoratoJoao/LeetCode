from collections import defaultdict


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