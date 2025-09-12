class Solution:
    def minimizedStringLength(self, s: str) -> int:
        n = ''
        for i in s:
            if i not in n:
                n+=i
        return len(n)
        