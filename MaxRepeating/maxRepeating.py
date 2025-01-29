def maxRepeating(sequence: str, word: str) -> int:
    count = 0
    while word * count in sequence:
        count += 1
    return count - 1

print(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba"
, "aaaba"))