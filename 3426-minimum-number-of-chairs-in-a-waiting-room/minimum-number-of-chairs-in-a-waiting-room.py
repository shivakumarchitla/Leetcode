class Solution:
    def minimumChairs(self, s: str) -> int:
        o = 0
        l=[]
        for i in s:
            if i == "E":
                o+=1
                l.append(o)
            elif i == "L":
                o+=-1
        return max(l)
            
        