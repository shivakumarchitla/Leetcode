class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n = ''
        l = ''
        for i in word1:
            n = n+i
        a = n
        for j in word2:
            l+=j
        b = l
        if a==b:
            return True
        else:
            return False

            
        