def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    numReversed = 0
    xCopy = x

    while xCopy > 0:
        lastDigit = xCopy % 10 # 123 % 10 = 3
        numReversed = numReversed * 10 + lastDigit
        xCopy //= 10 # 123 // 10 = 12, remove last digit
    return x == numReversed