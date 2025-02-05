function isPalindrome(x: number): boolean {
    if (x < 0) {
        return false;
    }
    let reversed = 0;
    let xCopy = x;
    while (xCopy > 0) {
        let lastDigit = xCopy % 10;
        reversed = reversed * 10 + lastDigit;
        xCopy = Math.floor(xCopy / 10);
    }

    return reversed === x;
};