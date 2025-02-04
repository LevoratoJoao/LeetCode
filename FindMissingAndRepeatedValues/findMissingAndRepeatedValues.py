from collections import defaultdict
from typing import List


def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    count = defaultdict(int)

    for i in grid:
        for j in i:
            count[j] += 1

    a, b = 0, 0
    for i in range(1, (len(grid) * len(grid) + 1)):
        if count[i] == 2:
            a = i
        elif count[i] == 0:
            b = i
    return [a, b]