class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        k = []
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    l = abs(i-j)
                    k.append(l)
        return max(k)


        