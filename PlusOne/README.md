# 66. Plus One

## Solution

Loop through the array from the end to the beginning. If the digit is 9 and N is 0 (meaning there is only one digit left) we change the digit at N to 1 and append 0 to the array. If the digit is 9 and N is not 0, we simply change the digit to 0. If the digit is not 9, we increment the digit by 1 and break the loop.

The time complexity is O(N) where N is the length of the array.

```python
def plusOne(self, digits: List[int]) -> List[int]:
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
```

We can also use the following solution which is more concise.

```python
def plusOne(self, digits: List[int]) -> List[int]:
    N = len(digits) - 1
    while N >= 0:
        if digits[N] == 9:
            digits[N] = 0
        else:
            digits[N] += 1
            return digits
        N -= 1

    return [1] + digits
```