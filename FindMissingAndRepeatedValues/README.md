# 2965. Find Missing and Repeated Values

## Solution

For this problem, we can use a hash table to store the frequency of each number. We iterate through the grid and increment the frequency of each number. Then we iterate from 1 to n * n (wich will be the total of numbers in the grid, e.g 1 to 9 for a 3x3 grid) and check if the frequency of the number is 0 or 2. If it is 0, then it is the missing number, if it is 2, then it is the repeated number.

```python
def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
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
```

Java code:

```java
public int[] findMissingAndRepeatedValues(int[][] grid) {
    HashMap<Integer, Integer> count = new HashMap<>();

    for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid.length; j++) {
            if (!count.containsKey(grid[i][j])) {
                count.put(grid[i][j], 1);
            } else {
                count.put(grid[i][j], count.get(grid[i][j]) + 1);
            }
        }
    }

    int a = 0;
    int b = 0;
    for (int i = 1; i < (grid.length * grid.length) + 1; i++) {
        if (count.containsKey(i) && count.get(i) == 2) {
            a = i;
        } else if (!count.containsKey(i)) {
            b = i;
        }
    }
    return new int[] { a, b };
}
```