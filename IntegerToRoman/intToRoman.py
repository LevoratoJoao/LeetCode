def intToRoman(num: int) -> str:
    symbols = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    res = ""
    for n, s in symbols.items():
        while num >= n:
            res += s
            num -= n
    return res

print(intToRoman(1994))
