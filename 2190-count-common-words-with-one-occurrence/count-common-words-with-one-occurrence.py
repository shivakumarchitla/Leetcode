class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        n = {}
        r = {}
        o = 0
        for i in words1:
            if i not in n:
                n[i] = 1
            else:
                n[i]+=1
        for i in words2:
            if i not in r:
                r[i] = 1
            else:
                r[i]+=1
        for j in n:
            if n[j]==1 and j in r and r[j]==1:
                o+=1
        return o


        