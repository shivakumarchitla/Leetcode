class Solution:
    def maxFreqSum(self, s: str) -> int:
        k = {}
        for i in s:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        l = []
        m = []
        for j in k:
            if j in "aeiou":
                l.append(k[j])
            else:
                m.append(k[j])
        return (max(l) if l else 0) + (max(m) if m else 0)
                



        