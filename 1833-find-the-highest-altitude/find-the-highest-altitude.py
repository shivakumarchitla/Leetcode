class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l = []
        l.append(0)
        for i in range(len(gain)):
            o=0
            for j in range(i,-1,-1):
                o+=gain[j]
            l.append(o)
        return max(l)


                
