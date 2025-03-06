class Solution:
    def backtrack(self, n: int, num: int, i: int):
        while num < n:
            num += 3**i
            i+=1
            if num == n:
                return i, num
        i = 0
        num = 0
        return i, num

    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        j = 0
        num = 0

        while num < n:
            i, num = self.backtrack(n, num, j)
            if i == 0:
                j += 1
        if num == n:
            return True
        return False

sol = Solution()
print(sol.checkPowersOfThree(12)) # True
print(sol.checkPowersOfThree(91)) # True
print(sol.checkPowersOfThree(21)) # False