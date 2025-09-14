class Solution:
    def finalString(self, s: str) -> str:
        m = ''
        for i in s:
            if i == "i":
                m = m[::-1]
            else:
                m +=i
        return m            
        