from typing import List


def plusOne(digits: List[int]) -> List[int]:
    N = len(digits) - 1
    while N >= 0:
        if digits[N] == 9 and N == 0:
            digits[N] = 1
            digits.append(0)
        elif digits[N] == 9:
            digits[N] = 0
        else:
            digits[N] += 1
            break
        N -= 1

    return digits

print(plusOne([4,3,2,1]))