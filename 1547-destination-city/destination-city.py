class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = []
        k = []
        for i in paths:
            n.append(i[0])
            k.append(i[1])
        for j in k:
            if j not in n:
                return j
                