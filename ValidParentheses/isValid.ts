function isValid(s: string): boolean {
    const hashMap = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    const stack: string[] = [];

    for (const i of s) {
        if (i === '(' || i === '[' || i === '{') {
            stack.push(i);
        } else if (!stack.length || stack.pop() !== hashMap[i]) {
            return false;
        }
    }
    return stack.length == 0;
};