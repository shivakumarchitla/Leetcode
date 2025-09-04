class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = {}
        k = []
        for i in arr:
            if i in n:
                n[i]+=1
            else:
                n[i]=1
        for i in n:
            if n[i]==i:
                k.append(i)
        if len(k)>0:
            return max(k)
        else:
            return -1
        