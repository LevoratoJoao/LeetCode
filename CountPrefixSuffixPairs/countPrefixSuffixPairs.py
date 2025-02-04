from typing import List

def isPrefixAndSuffix(word_i, word_j):
        if len(word_i) > len(word_j): return False
        return word_j.startswith(word_i) and word_j.endswith(word_i)

def countPrefixSuffixPairs(words: List[str]) -> int:
    N = len(words)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if isPrefixAndSuffix(words[i], words[j]):
                ans+=1
    return ans

print(countPrefixSuffixPairs(["a","aba","ababa","aa"]))