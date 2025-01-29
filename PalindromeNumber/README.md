# 9. Palindrome Number

## Reverse and Compare

First we check if the number is negative, since negative numbers are not palindromes. Then we begin reversing the number. We initialize a variable with 0 and a copy of the number, then we loop through the number until his value is 0. In each iteration we get the last digit by moding the number by 10 e.g. `123 % 10 = 3`, then we multiply the reversed number by 10 and add the last digit to it. Finally we divide the number by 10 to remove the last digit and continue the loop. At the end we compare the reversed number with the original number.

```python
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    numReversed = 0
    xCopy = x

    while xCopy > 0:
        lastDigit = xCopy % 10
        numReversed = numReversed * 10 + lastDigit
        xCopy //= 10
    return x == numReversed
```

- Time Complexity: O(log(x))
- Space Complexity: O(1)

## Other Solutions

- Another solution is to convert the number to a string and use two pointer to compare it.
- A more efficient solution is to reverse only half of the number and compare it with the other half.