def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    stack = []
    close_brackets = {")":"(", "]":"[", "}":"{"}
    for i in s:
        if i in close_brackets.values():
            stack.append(i)
        elif len(stack) == 0 or stack.pop() != close_brackets[i]:
            return False
    return len(stack) == 0

print(isValid("()")) # True