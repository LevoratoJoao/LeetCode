def isPalindrome(s: str) -> bool:
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < j:
        if s[j] == s[i]:
            i+=1
            j-=1
            continue
        else:
            if not s[j].isalnum():
                i+=1
            elif not s[i].isalnum():
                j-=1
            else:
                return False
    return True
