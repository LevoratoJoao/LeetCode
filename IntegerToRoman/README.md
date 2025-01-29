# 12. Integer to Roman

## Solution

First create a HashMap with the values of the roman numerals in descending order, e.g. `1000: 'M'`, `900: 'CM'`, `500: 'D'`, `400: 'CD'`, etc. Then iterate through the HashMap (number and symbol), after that we check if the given num is greater then the current number of the HashMap, if it is we add that symbol to the result and subtract the. If it is not we move to the next number in the HashMap.

```python
def intToRoman(num: int) -> str:
    romanNumerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for number, symbol in romanNumerals.items():
        while num >= number:
            result += symbol
            num -= number
    return result
```

- Time Complexity: O(1)
- Space Complexity: O(1)