class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = ''
        x = str(x)
        for i in range(len(x)):
            n = x[i]+n
        if n == x:
            return True
        else:
            return False
        