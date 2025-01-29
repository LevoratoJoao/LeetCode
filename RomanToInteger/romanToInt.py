# S: O(N)
# M: O(1)
def romanToInt(s: str) -> int:
    symbols = { "I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    number = 0
    N = len(s)
    i = 0
    while i < N:
        if i < N - 1 and symbols[s[i]] < symbols[s[i + 1]]:
            number += symbols[s[i + 1]] - symbols[s[i]]
            i += 2
        else:
            number += symbols[s[i]]
            i += 1
    return number